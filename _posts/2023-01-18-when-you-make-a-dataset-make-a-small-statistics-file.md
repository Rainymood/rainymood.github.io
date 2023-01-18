---
title: "When you make a dataset, make a small statistics file"
date: 2023-01-18
tags:
- python
- sql
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2023-01-18-when-you-make-a-dataset-make-a-small-statistics-file/thumbnail.png"
---

This is another lesson that I learned building machine learning systems. For the other lessons that I learned click [here]({% post_url 2022-12-21-lessons-learned-from-building-machine-learning-systems %}).

![](/../assets/2023-01-18-when-you-make-a-dataset-make-a-small-statistics-file/2023-01-18-15-53-28.png)

**When you are creating a data set, make a small statistics file.**

I learned this the hard way. When you are creating your dataset, make sure to also create a file that contains the most important statistics of this dataset at the time of creation. At the very least you want to have the minimum, maximum, count, and number of unique values per variable that you have.

For me, the number of unique values is very important because I often end up making embeddings. And to make embeddings you need to know how much values you want to embed. 

But really, this file can be anything ranging from a pickled dictionary to a dataframe or just some plain old text. Trust me, you will need these values later down the line. This is especially important when your dataset becomes big because then it can take nontrivial time to actually create the dataset. 

So, keep in mind when you are creating a dataset to make a small statistics file! 

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
    