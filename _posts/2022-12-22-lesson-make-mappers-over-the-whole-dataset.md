---
title: "Lesson: Make mappers over the whole dataset"
date: 2022-12-22
tags:
- python
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2022-12-22-lesson-make-mappers-over-the-whole-dataset/thumbnail.png"
---

Another lesson that I learned the hard way building machine learning systems is this: **build your mappers over the whole dataset (and not for train and test separately)**.

We need to use mappers because our data often does not come in a nice and dense format by default. Let me show what I mean with a "dense" format. Imagine our dataset has 3 users:

```
users = ["Alice", "Bob", "Clyde"]
```

To model this, we need a mapper that maps each user to a number, ideally in a nice and compact range without any gaps, that is what we think of something being dense. This is the mapper we are looking for: 

|userid|userid_dense
|-|-|
|Alice|0|
|Bob|1|
|Clyde|2|

Now we can actually start modeling the data.

A mistake I made early on in one of my projects was that I separated the data into `train` and `test` and I also tried to build mappers over these datasets, like `train_mapper` and `test_mapper`. 
This turned out to be an annoying mistake and caused a lot of duplication. We quickly god rid of it, thankfully, but this is another lesson I don't want to forget.

Two more tiny notes: 
* Mappers are key to any non-trivial machine learning problem and your mappers are intricately connected to a single dataset, so store them together as well. 
* However, you have to be mindful of values that are not in your mapper. How are you going to handle them? Imagine if you train a model on these users, what if you find a user that is not in your dense userid list? How are you going to handle that? 


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
    