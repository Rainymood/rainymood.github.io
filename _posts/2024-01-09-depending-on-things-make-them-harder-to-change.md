---
title: "Depending on things make them harder to change"
date: 2024-01-09
tags:
# Blog or how-to
- blog

# Work or personal?
- personal

# Big themes that I write about
- systems

categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2024-01-09-depending-on-things-make-them-harder-to-change/thumbnail.png"
---
<!-- ctrl + alt + v -->

<!-- Checklist:
Title = insight
Interesting 1st sentence
Short and concise -->

<!-- 1. interesting hook -->
The more you start to use things, depend on them, the harder they become to change.

This story starts with a data lake that all the scientist use. The data lake is created somewhere upstream (bubble) and it just happily exists somewhere and it has all the data we need. The data scientists can query this data lake and people live happily ever after.

![](/../assets/2024-01-09-depending-on-things-make-them-harder-to-change/2024-01-10-06-45-46.png)

Years went by and as the team grew the data scientists started creating **production services** using this data lake. Most of these systems just pull some data from there, do things with it, and store that information somewhere else. These systems are Zap, Bar, and Foo respectively. 

![](/../assets/2024-01-09-depending-on-things-make-them-harder-to-change/2024-01-10-06-45-59.png)

Now, there’s a lone and sad data engineer that needed to make an important change to the data lake. But after working on this for weeks he has come to the realisation that it is simply too much work to make this change. Why? Because now that three production services depend on it, any change in the data lake must be propagated in the services using it, but the people maintaining Zap, Bar, and Foo are long gone, and no one knows how to do it.

![](/../assets/2024-01-09-depending-on-things-make-them-harder-to-change/2024-01-10-06-46-10.png)


A small change in the data lake is now a big change in the whole system because we depend on the data lake. 

**The moral of the story is: if you start depending on something, it becomes harder to change.**

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
    