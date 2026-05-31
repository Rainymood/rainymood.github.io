---
title: "How we made our model warmup 168x faster"
date: 2026-05-29
tags:
# Work or personal?
- work
- personal

# Start here themes
- systems
- software
- learning
- product
- career

# Series
- recently
- practical-advice
- how-I-use-AI

# Big themes that I write about
- artificial intelligence
- complexity
- engineering
- software architecture
- management
- leadership
- productivity
- lean
- memory palace

# Programming languages/Cloud
- advent of code
- rust
- golang
- python
- sql
- javascript
- aws
- testing
- documentation

# Smaller themes
- book summary
- writing
- product
- design
- tools
- advent of code
- aws 
- docker
- machine learning
- programming
- pytorch
- tensorflow
- code
- show-your-work
- tip
- athena
- flashcards
- projects
- startups
- domain driven design
- story
- lessons learned
- video games

# Gamedev
- unity
- gamedev
- juice

categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2026-05-29-how-i-made-our-model-warmup-168x-faster/thumbnail.png"
---
<!-- ctrl + alt + v -->
<!-- cmd + alt + v -->

In this blog post I want to tell the story about how we **sped up our model warmup by 168x**. 

I recently pulled up the numbers and honestly I was kind of shocked myself. I didn't realize we had sped it up so much.

* Before: 1 year of data. 50k users. 48 hours. 
* After: 7 years of data. 150k users. 6 hours. (7 times more data, 3 times more users, 8 times faster = 7 x 3 x 8 = 168x)

Then the question is. How did we do this?

# Trick 1 (fixed width csv bytes ranges)

The first trick we pulled out of our sleeves to do this was a custom data format. Our data processing routine created fixed with csv files.

We created files that looked like this, with the `#` for padding.

```csv
12345,1,1,98765,2024-01-15T10:30:00,2024-01-15,################,5,2019,2,42
12345,0,0,98766,2024-01-15T10:31:00,2024-01-15,################,5,2019,2,42
999999999,1,1,100000001,2024-01-15T11:00:00,2024-01-15,#######,5,2019,2,42
```

Each row is now 111 characters fixed with. Note that specifically the last row has only 109 characters. This is to reserve 1 character for the `/n` newline character! We learned this the hard way. 

This is the full flow of the csv byte range trick:

1. We padded all the data to `111` chars
2. We built an `interval` table that had the `start_bytes` and `end_bytes` per interval, with one file having multiple intervals
3. We pull data from s3 using `Range: bytes=X-Y` to fetch only the rows we needed

```python
response = self.s3_client.get_object(Bucket=bucket, Key=key,
Range=f"bytes={start_bytes}-{end_bytes}")
```

Now we have one large file for each user where one interval is a week worth of data. Based on our table creation logic we can split the data as follows

```
start_bytes = first_row_index * 111
end_bytes   = (last_row_index + 1) * 111 - 1
```

We iterated on several solutions and this was the fastest way we could read the data by far.

# Trick 2 (optimized batches)

We created a new type of data structure that resembles a heap. It maintains an ordered list of users and their intervals. 

```python
# 5 pupils, each with their intervals: (answer_count, message_id)
intervals = {
    "alice":   [(200, 0), (50, 1)],   # 2 intervals: 200 answers, then 50
    "bob":     [(180, 2), (60, 3)],   # 2 intervals: 180, then 60
    "charlie": [(190, 4)],            # 1 interval:  190 answers
    "diana":   [(30, 5)],             # 1 interval:  30 answers
    "eve":     [(25, 6)],             # 1 interval:  25 answers
}

# Heap strategy: prioritize pupils with most intervals, then longest next interval
def strategy(v):
    return (-len(v), -v[0][0])

heap = IntervalHeapDict(intervals, key_fn=strategy)

batch_num = 0
while len(heap) != 0:
    batch = heap.take_next_batch()
    batch_num += 1
    lengths = [x[0] for x in batch]
    padding_pct = (max(lengths) * len(lengths) - sum(lengths)) / (max(lengths) * len(lengths))
    print(f"Batch {batch_num}: {len(batch)} pupils, lengths={lengths}, padding={padding_pct:.0%}")
```

Which would result in something like 

```python
Batch 1: 3 pupils, lengths=[200, 180, 190], padding=5%
Batch 2: 3 pupils, lengths=[50, 60, 30],    padding=44%
Batch 3: 1 pupil,  lengths=[25],            padding=0%
```


https://app.bannerbear.com/projects/POobgvMNDkxzxAYW70/templates/3g8zka5Y2OlaDEJXBY

https://www.photopea.com/

# Trick 3 (massive parallelization)

The third trick we applied was massive parallelization. 

We considered the two extremes. The first extreme is where we have as much lambdas as groups. Then the other end of the extreme was where we had only 1 lambda and we did everything in sequence. We were doingit for 3 of our subjects so we knew that we had 3 groups already. The question is now: how much groups could wem ake?

We realized that we could split up the work and cut it up as much as we wanted.




# Subscribe

<!-- Begin Mailchimp Signup Form -->
<link href="//cdn-images.mailchimp.com/embedcode/horizontal-slim-10_7.css" rel="stylesheet" type="text/css">
<style type="text/css">
#mc_embed_signup{background:#fff; clear:left; font:14px Helvetica,Arial,sans-serif; width:100%;}
/* Add your own Mailchimp form style overrides in your site stylesheet or in this style block.
    We recommend moving this block and the preceding CSS link to the HEAD of your HTML file. */
</style>
<div id="mc_embed_signup">
<form action="https://gmail.us3.list-manage.com/subscribe/post?u=92fe86c389878585bc87837e8&amp;id=50543deff9" method="post" id="mc-embedded-subscribe-form" name="mc-embedded-subscribe-form" class="validate" target="_blank" novalidate>
    <div id="mc_embed_signup_scroll">
<label for="mce-EMAIL">I blog about how to grow as a machine learning engineer! Liked this article and want to hear more? Join 40+ others and subscribe!</label>
<input type="email" value="" name="EMAIL" class="email" id="mce-EMAIL" placeholder="email address" required>
    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
    <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_92fe86c389878585bc87837e8_50543deff9" tabindex="-1" value=""></div>
    <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button"></div>
    </div>
</form>
</div>
<!--End mc_embed_signup-->
    