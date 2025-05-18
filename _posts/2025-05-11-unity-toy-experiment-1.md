---
title: "Unity toy experiment 1"
date: 2025-05-11
tags:
# Blog or how-to
- blog
# Gamedev
- unity
- gamedev
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2025-05-11-unity-toy-experiment-1/thumbnail.png"
---
<!-- ctrl + alt + v -->

I started toying around in [Unity](https://unity.com). 

I'm a complete beginner so I noticed I was really missing a lot of conceptual knowledge of what goes where. What is a scene? What is a canvas? How do you make UI etc. I decided I would build a small "game" that you can "play" from the menu. It would take you to a game screen with a button and then when you click the button there it would exit the game.

Voila. 

![](/../assets/2025-05-11-unity-toy-experiment-1/2025-05-11 07-41-32.gif)

Learning goals

* Learn how different scenes work
* Learn how we can move between scenes and exit the game

Reflection

* I learned what I wanted to learn which was a) how scenes work and b) how to move through them
* The next step for a tiny project is adding some state, maybe some scores or high scores to understand how data flows
* Even with such a tiny project there was enough to figure out, specifically with how the buttons are wired up using C#.
* This project was tiny and well-scoped which made it actually easy to finish which I think is underrated maybe

[Simon Willison](https://simonwillison.net/2022/Nov/6/what-to-blog-about/#projects) advises to write about your projects, so here I am.
    
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
    