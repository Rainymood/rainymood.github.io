---
title: "A tale of two values"
date: 2024-01-19
tags:
# Blog or how-to
- blog

# Work or personal?
- work

# Big themes that I write about
- systems
- architecture
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2024-01-19-a-tale-of-two-values/thumbnail.png"
---
<!-- ctrl + alt + v -->

<!-- Checklist:
Title = insight
Interesting 1st sentence
Short and concise -->

<!-- Do the most annoying thing first: thumbnail creation -->
What is more important? The current behaviour of the system (functionality) or the ability of the system to change (architecture)?
This is the trade-off that software architects have to keep in mind with every decision both big and small. 

People from the business will often tell you that current function and behaviour is more important because it delivers added user value right now. But if you always relent to this pressure then you are failing at your job of being a software architect. 

Whatever you do there will always be more and more requests from the business to respond to changing market conditions, but if you don’t draw a line in the sand and if you keep giving in, then at some point all chose changes make the system so hard to change that everything will grind to a halt. Then people from the business will look and you, scoff, and think: he did a terrible job for not saying no more often to us. 

It’s your responsibility to both (a) make the required changes but even more importantly (b) keep the system in such a healthy state that it is possible to do (a). That is the principal task of a software architect. This means sometimes saying no to requests from the business in order to protect the long-term integrity of the system.

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
    