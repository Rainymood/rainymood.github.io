---
title: "Sweat the Small Stuff"
date: 2025-01-04
tags:
# Blog or how-to
- blog
# Work or personal?
- work
- systems
- complexity
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2025-01-04-sweat-the-small-stuff/thumbnail.png"
---
<!-- ctrl + alt + v -->

Complexity is incremental. So is quality. So sweat the small stuff.

![](/../assets/2025-01-04-sweat-the-small-stuff/2025-01-04-16-15-44.png)

Every change you make to a system that makes it less complex is a direct increase in quality.

For example: If we define a variable `batch_size=10`, we can make it more precise by renaming it to `batch_size=BatchSize(10)` where `BatchSize` is a new type wrapper over an `int`. This naming is more precise, which is less complex, an increase in quality.

Sweating the small stuff, all the little details and steps in the right direction, they add up to something meaningful. Every step in the right direction that makes your system less comlex increases quality in some way or another, even if the individual steps seem almost trivial. Together they add up.

What helps with sweating the small stuff is striving for perfection every time. Although perfection is an unattainable goal, it will help you to sweat the small stuff. Why? Because it contrasts the current state of your system against a perfect unattainable ideal. This gives you a direction to improve in. So rename that one variable. Refactor that small function. Write that single missing unit test. 

All the little things you do, they truly **do** add up, they truly **do** matter.

Complexity is incremental. So is quality. So sweat the small stuff.

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
    