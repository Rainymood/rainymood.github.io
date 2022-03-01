---
title: "How to scale up your code"
date: 2022-03-01
categories:
  - blog
toc: false
toc_sticky: false
header:
  teaser: "/../assets/2022-03-01-how-to-scale-up-your-code/thumbnail.png"
---

As a machine learning engineer it is part of your job to run things on large data sets.

When your datasets are small, life is good. Everything works and nothing breaks.

Sadly, however, sometimes your datasets become big, like, really big. And thats when trouble starts. 

It is your job as a machine learning engineer to figure out how to deal with this and to make your algorithms run on big datasets.

Thankfully some very smart people have thought about this and I'm just here to share their knowledge :)

This is your happy land. Your code and algorithm snugly fit in memory.

![](/../assets/2022-03-01-how-to-scale-up-your-code/2022-03-01-14-56-04.png)

But now, behold, danger! 

You scaled up your dataset from 1 million rows to 10 billion rows and it doesn't fit in the memory anymore :(

![](/../assets/2022-03-01-how-to-scale-up-your-code/2022-03-01-14-56-25.png)

What to do now...

When you think about there are only two ways we can deal with this:

1. Increase memory available (i.e. throw $$$ at the problem)
2. Reduce memory usage 

## Option 1: Throw money at the problem

The most straightforward solution is to just increase the memory that we have. 

![](/../assets/2022-03-01-how-to-scale-up-your-code/2022-03-01-14-58-35.png)

This could mean buying a bigger machine, GPU, or even moving to the cloud.  In other words, you throw money at the problem. 

I kind of joke about it but throwing money at the problem can actually be a very good solution because as a developer your time is expensive. So consider the trade-off of just increasing your memory over min-maxing the memory usage.

Throwing money at the problem works for sure but it's in my opinion better to first try to reduce the memory usage a bit and *then* to scale up with more money.

## Option 2: Reduce memory usage

The second option you have available is not to increase the memory that we have. But to reduce the memory usage of the program in the current memory

![](/../assets/2022-03-01-how-to-scale-up-your-code/2022-03-01-15-00-10.png)

This is often not easy, but hey, this makes it also fun, right :)

Here are the three most important and practical techniques to reduce your program's memory footprint:

1. **Compression.** Compression means using a different representation for your data that uses less memory. The question you need to ask is this: Can you represent the data the same way but in a different smaller format? For example, moving from a big sparse matrix to a dense vector mapping often seems to work wonders.
2. **Chunking.** Chunking means loading the data in one chunk at a time instead of all at once. The question you need to ask here is do we really need all the data at once? Or can we load in the data bit by bit? I would almost put gradient descent in this bucket. Instead of loading in all the data at once we load in batches, compute the loss on that batch, and update the gradients accordingly. There you have it, chunking.
3. **Indexing.** Indexing means loading only the subset of the data that you need, by constructing an index of data that you need beforehand. For example, say you are reading a book and want to search for the word `Roman`. You could solve this with chunking (load in the book page by page) but it is much better to just go to the back of the book and search for `Roman` in the index. That is indexing.

# Conclusion

What to do if your data doesn't fit in your memory anymore:

1. Increase your memory
   1. Throw $$$ at the problem
2. Reduce your memory usage
   1. Compression: find a different smaller representation of your data
   2. Chunking: load in the data chunk by chunk
   3. Indexing: build an index of data you need and only load that

If you are looking for speedups, my personal recommendation is to first try **compression** followed by **chunking** and then just **throwing $$$ at the problem**. 

This post is a summary of [this](https://pythonspeed.com/articles/data-doesnt-fit-in-memory/), so be sure to check that out. I went quite light on the details here :)

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
  <label for="mce-EMAIL">Liked this article and want to hear more? Join 40+ others and subscribe!</label>
  <input type="email" value="" name="EMAIL" class="email" id="mce-EMAIL" placeholder="email address" required>
    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
    <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_92fe86c389878585bc87837e8_50543deff9" tabindex="-1" value=""></div>
    <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button"></div>
    </div>
</form>
</div>
<!--End mc_embed_signup-->
