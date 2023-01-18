---
title: "Make sure you can find back your mlflow runs"
date: 2023-01-18
tags:
- python
- machine learning
- mlflow
- lessons learned
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2023-01-18-make-sure-you-can-find-back-your-mlflow-runs/thumbnail.png"
---

Here's another lesson that I learned about building machine learning systems. For the full overview of the lessons, click [here]({% post_url 2022-12-21-lessons-learned-from-building-machine-learning-systems %}).

![](/../assets/2023-01-18-make-sure-you-can-find-back-your-mlflow-runs/2023-01-18-16-10-05.png)

The lesson that I want to give you today is that **you should be able to find back the machine learning runs that you did**.

Doing runs and storing them in mlflow is not enough. Because this doesn't mean you can find them back later. 

I recently ran into this myself. To make an important decision on which model we wanted to continue developing I had to make an overview of all the models we previously trained. I thought we were good because we had mlflow, but in practice it turned out to be quite difficult to match mlflow runs to the actual experiments we performed. 

It was difficult because we had so many different runs and different iterations and stored everything together in a single mlflow experiment. All in all, I wish I was a bit more disciplined while actually storing the runs so that it would save me time later. 

So this is the trick that I want to give you: **add your ticket number that you are working on as a parameter in mlflow**. You are most likely using some form of Kanban where each ticket has some form of unique id, so why not use it? Next time, when you are browsing your old runs you can filter on each of these ids to pare down your search results. This makes linking old runs to actual experiments you did a lot easier because this work is often specified in the ticket.

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
    