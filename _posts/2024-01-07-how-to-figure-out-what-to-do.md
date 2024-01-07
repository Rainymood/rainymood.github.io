---
title: "How to figure out what to do "
date: 2024-01-07
tags:
# Blog or how-to
- blog
- tutorial

# Work or personal?
- work
- personal

# Big themes that I write about
- engineering
- management
- leadership
- systems
- productivity

# Programming languages/Cloud
- golang
- python
- sql
- javascript
- aws
- testing

# Smaller themes
- writing
- product
- design
- tools
- learning

- advent of code
- aws 
- docker
- machine learning
- programming
- pytorch
- tensorflow
- code
- show-your-work
- tip
- athena

- meta programming
- architecture

- flashcards
- projects
- startups

- cosmicpython
- inversion of control
- domain driven design

- story
- lessons learned
- video games

categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2024-01-07-how-to-figure-out-what-to-do/thumbnail.png"
---
<!-- ctrl + alt + v -->

<!-- Checklist:
Title = insight
Interesting 1st sentence
Short and concise -->

<!-- 1. interesting hook -->
Let’s face it, sometimes we are stuck and we do not know what to do. This can feel terrible and I want to give you a simple system to help you figure out where to look first to unstuck yourself.

Most things in life involve answering (at the least) these two questions. The first question is: “What do we need to do?” (requirements gathering). The second question is: “How will we do it?” (designing or specifying).

> *"The hardest single part of building a software system is deciding what to build. No other part of the conceptual work is as difficult in establishing the detailed technical requirements, including the interfaces to people, to machines, and to other software systems. No other part of the work so cripples the results if done wrong. No other part is more difficult to rectify later. Therefore, the most important function that the software builder performs for the client is the iterative extraction and refinement of the product requirements."* —Fred Brooks

The basic planning process in software engineering revolves around these two steps, first gathering requirements and then designing a solution to meet those requirements. 

A requirement is a carefully written down description of a criteria that the work is supposed to satisfy. There might be many ways a design can satisfy a requirement, but it should be straightforward to see if the requirement has been met by looking at the finished piece of work. A specification or design is then simply a plan for building something that will satisfy the requirement. 

And... that's the framework. That's it. 

![](/../assets/2024-01-07-how-to-figure-out-what-to-do/2024-01-07-07-07-05.png)

(*Image: Making Things Happen by Scott Berkun*)

That diagram right there is the framework in figuring out what to do. 

Why? 

Because now when you are stuck you can place yourself into either one of these three categories:

* Do you not know **what** to do? That means that the requirements are unclear, then figure that out. 
* Do you not know **how** to do it? That means that you need some help with your design, then figure that out. 
* Do you know what and how but you just need to **do** it now? That’s a motivation problem, figure that out.

Final note, I also like is that this maps almost 1:1 to the PRD and RFC framework that Hashicorp describes in this blog post [How HashiCorp Works](https://works.hashicorp.com/articles/writing-practices-and-culture).

![](/../assets/2024-01-07-how-to-figure-out-what-to-do/2024-01-07-07-01-04.png)

*Remixed and adapted from Making Things Happen by Scott Berkun. There might be some words in here that I straight up copied, but I found the framework so useful to figure out what to do I wanted to share it anyway.*

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
    