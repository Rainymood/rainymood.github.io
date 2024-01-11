---
title: "How to speed up your code"
date: 2024-01-10
tags:
# Blog or how-to
- tutorial

# Work or personal?
- work

# Big themes that I write about
- engineering
- programming
- code
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2024-01-11-how-to-speed-up-your-code/thumbnail.png"
---
<!-- ctrl + alt + v -->

<!-- Checklist:
Title = insight
Interesting 1st sentence
Short and concise -->

<!-- 1. interesting hook -->
Speed in and of itself can be a feature, see [ruff](https://github.com/astral-sh/ruff) for example. Here's a list of tricks that I've found useful to speed up your code.

![](/../assets/2024-01-11-how-to-speed-up-your-code/2024-01-11-06-43-57.png)

1. **Profile.** The first rule of profiling is to never trust your gut. The computer works in mysterious ways and the bottleneck might not be where you think it is. Profile first and really measure what is slow.
2. **Don’t do it (elimination).** The best code is code that doesn’t exist. Speed up your code by removing things. Are there calculations or steps that you can skip?
3. **Do it once (caching).**  Can we speed things up by doing them once? Can we remove duplicate work? Is there work that you can do and then cache/remember the result and reuse that? 
4. **Do it once 2 (pre-computing).** Can we speed things up by doing some calculations before we start the routine on disk as opposed to caching in memory?
5. **Do it efficiently (vectorisation/parallelization).** Can we do things more efficiently? Can we exploit matrix structures instead of doing things on single rows? Can we do steps at the same time that we are doing sequentially now?
6. **Do it less accurately (quantization).** Can we be less accurate? Can we quantize the model? Can we reduce precision from a float32 to float16 or float8? Can we sacrifice some accuracy for speed? Are there other knobs and trade-offs that can speed things up like reducing some other parameters.

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
    