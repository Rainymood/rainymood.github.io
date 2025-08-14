---
title: "How we made our CICD pipelines 30% faster by putting things in parallel"
date: 2025-08-14
tags:
# Blog or how-to
- blog
- work
# Start here themes
- systems
- software
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2025-08-14-how-we-made-our-cicd-pipelines-30-faster-by-putting-things-in-parallel/thumbnail.png"
---
<!-- ctrl + alt + v -->
<!-- cmd + alt + v -->

I wrote this post in July of 2024... which is more than a year ago! 

But the lesson still remains true. 

Always ask yourself this: What can be done in parallel? What **must** be done in sequence? 

Sometimes low-hanging fruit is really low-hanging. A while ago I managed to reduce our pipelines by 12 minutes (yes 12 minutes) by just putting things in parallel that could be done in parallel.

This was our pipeline before:

![](/../assets/2025-08-14-how-we-made-our-cicd-pipelines-30-faster-by-putting-things-in-parallel/2025-08-14-17-56-05.png)

I realized that there was *no reason whatsoever* for both the Package and Copy Model Artifacts step to be in sequence with Build, Test & Analyze, so I put them in sequence!

![](/../assets/2025-08-14-how-we-made-our-cicd-pipelines-30-faster-by-putting-things-in-parallel/2025-08-14-17-56-16.png)

That's it. The same pipeline, just 12 minutes and 9 seconds faster.

What can be done in parallel? What **must** be done in sequence?

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
    