---
title: "Reducing our stored model state by 80% using bit manipulation magic in Python"
date: 2024-07-28
tags:
# Blog or how-to
- tutorial

# Work or personal?
- work

# Start here themes
- software

# Big themes that I write about
- engineering

- python

categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2024-07-28-reducing-oour-stored-model-state-by-80-using-bit-manipulation-magic-in-python/thumbnail.png"
---
<!-- ctrl + alt + v -->

This week was pretty cool, together with a bearded grey wizard on our data engineering team we managed to reduce the model state we have to store by roughly 80% from 18kb to 4kb.

This was pretty wild, but also pretty necessary, because this is part of an API that will be called around 20 million times a day.

For some context, I'm working in the machine learning infrastructure team at my company and we are currently revamping our complete architecture how we host and productise models. 

One of our core tasks as a machine learning platform is storing and retrieving model state, and because this happens so often (with every model call) we need to do this fast and efficiently.

We (the platform team) care about how things run in production, the data science team... not so much. To our horror we realized that the data science team added this thing called the `answer_type_count` to the state they wanted to store.


```python
@dataclass
class ModelState(PupilState):
    answer_count: int
    answer_type_counts: Dict[str, List[int]] # <==  new
    focus_ability: float
    skill_state: List[float]
```

We thought this was fine, but when we started looking at some production json payloads with the envisioned embedding sizes we realized that this would be a problem because the `answer_type_counts` was a vector of 3000 integers! Storing this extra data every API call would be a disaster and explode our costs.

I was in a meeting with our PO and the wise greybeard from the data engineering team and the core message of that meeting was: we have to get this payload down. The greybeard said "No problem, let's get to work."

The first thing the greybeard quizzed me on was about the numbers: "What's the current payload size? What kind of numbers do we have? How many do we need to store? Do we need to store all of them? Can we store a subset of them?"

I answered them in rapid succession. "Current payload size is 18kb. We need to store ints. Around 3000 of them. The maximum int we need to store is 101 because that's the last embedding that the model uses..." 

When I said this, his eyes lit up. He continued: "That's great news, because we can count to 2, 4, 8, ... we can count to 255 with just 8 bits. So if we need to store just 101 we only need 7 bits, but for simplicity let's just take the first 8 bits or the first byte."

Now look. Here I am kind of like a fish out of the water. This felt like low-level black magic to me, really diving deeps into the bits and bytes and only taking what is truly necessary. I was eager to help out where possible.

I knew that by default Python stores its integers in 32 bit format. So I said: "So do I understand it correctly that what you're saying is that instead of using the 32 bit integer, we can just chop off the first 4 bytes and only take the last byte? Because we need to count to 101?"

"Yup," the greybard replied.

"How do we do this?" I asked.

The greybard explained that we could take the list of ints and pack together the contents as bytes, converting them to [unsigned chars](https://docs.python.org/3/library/struct.html#format-characters) using `struct`. 

Compressing this list of integers then looks something like this

```python
>>> lst = [1, 2, 3]
>>> capped = [min(x, 101) for x in lst]
>>> compressed = base64.b64encode(zlib.compress(struct.pack("<" + "B" * len(capped), *capped))).decode("utf-8")
>>> compressed
eJxjZGIGAAANAAc=
```

So we convert the list `[1,2,3]` to the string `"eJxjZGIGAAANAAc="`. 

Let's run through this code line by line: 

* `[min(x, 101) for x in lst]` caps the elements to a maximum of 101 
* `struct.pack()` with converts the elements in the list to unsigned chars (`"B"`) in the little endian form (`"<"`) allowing us to only store 8-bits or 1-byte per integer
* `zlib.compress()` compresses these bytes even further, this is especially powerful when the list contains a lot of repetition
* `base64.b64encode` then encodes the bytes into a format that we can send over the web (i.e. as a stringified json)

What's really cool is that the more repetition we have in the list, the better the compression. 

```python
lst = 10_000 * [0, 1]
capped = [min(x, 101) for x in lst]
compressed = base64.b64encode(zlib.compress(struct.pack("<" + "B" * len(capped), *capped))).decode("utf-8")
size_with = len(compressed) # 60
size_without = len(json.dumps(lst)) # 60_000
```

Decompressing is just doing everything the other way around.

```python
>>> bs: bytes = zlib.decompress(base64.b64decode(compressed))
>>> lst = list(struct.unpack("<" + "B" * len(bs), bs))
>>> st
[1, 2, 3]
```

Applying this "simple" compression algorithm is what pushed the state down from 18kb to 4kb, a rough 80% reduction in size, amazing. Really cool stuff.

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
    