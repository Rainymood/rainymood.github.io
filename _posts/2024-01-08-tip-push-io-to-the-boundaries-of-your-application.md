---
title: "Tip: Push IO to the boundaries of your application"
date: 2024-01-08
tags:
# Blog or how-to
- blog

# Work or personal?
- work

# Big themes that I write about
- engineering
- programming
- tip
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2024-01-08-tip-push-io-to-the-boundaries-of-your-application/thumbnail.png"
---
<!-- ctrl + alt + v -->

<!-- Checklist:
Title = insight
Interesting 1st sentence
Short and concise -->

<!-- 1. interesting hook -->
Some things people only learn the hard way, this is a lesson I learned the hard way by making this mistake one too many times.

![](/../assets/2024-01-08-tip-push-io-to-the-boundaries-of-your-application/2024-01-08-06-41-56.png)

Here's a nice tip: **Push all your data input output (IO) to the boundaries of your application**. What this means is that you want all your reads and writes to be defined in the "outer" layer of your application. If you find a `pd.read_csv()` somewhere in the middle of your code of one of your embedding layers then something is wrong. What you should have done was define this IO operation at the top (near the entrypoint) and then create an object that represents that thing and pass that around. 

This tip is very closely related to these two great blogs:

* [Impureim sandwich](https://blog.ploeh.dk/2020/03/02/impureim-sandwich/):
* [Improve your code by separating mechanism from policy](https://lambdaisland.com/blog/2022-03-10-mechanism-vs-policy):

The basic gist is that there is a difference between impure (and policy) code and pure code and that we must separate the two. If you put your IO somewhere in our pure code your are mixing things that should not be mixed, like oil and water.

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
    