---
title: "A Tale of Two Values"
date: 2023-02-24
tags:
- architecture
- programming
- tools
- motivation
- flashcards
- pytorch
- tensorflow
- learning
- projects
- python
- sql
- product
- startups
- life
- machine learning
- aws 
- docker
- lessons learned
- story
- cosmicpython
- inversion of control
- code
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2023-02-24-a-tale-of-two-values/thumbnail.png"
---

In our quest to write good software that is functional, testable, and maintainable, we must first understand what makes a system good. What separates a good software system from a bad software system? A lot of it has to do with how flexible it is as we will see in this next parable. 

This is a chopped up and remixed version of a chapter called *A Tale of Two Values* from the book [Clean Architecture](https://en.wikipedia.org/wiki/Hexagonal_architecture_(software)).


> Function or architecture? Which of these two provides the greater value? Is it more important for the software system to work, or is it more important for the software system to be easy to change?

It starts by asking the following question: Which of these two values is more important in any software system? That it works, or that it is easy to change?

> If you ask the business managers, they’ll often say that it’s more important for the software system to work. Developers, in turn, often go along with this attitude. But it’s the wrong attitude. 

If you ask business people, they will say that function is the greater value of the two. But we can "disprove" that with [reductio ad absurdum](https://en.wikipedia.org/wiki/Reductio_ad_absurdum).

> I can prove that it is wrong with the simple logical tool of examining the extremes.
> - If you give me a program that works perfectly but is impossible to change, then it won’t work when the requirements change, and I won’t be able to make it work. Therefore the program will become useless.
> - If you give me a program that does not work but is easy to change, then I can make it work, and keep it working as requirements change. Therefore the program will remain continually useful.

In other words, because in any realistic system the business requirements change over time, we argue that flexibility is more important than functionality. 

> You may not find this argument convincing. After all, there’s no such thing as a program that is impossible to change. However, there are systems that are practically impossible to change, because the cost of change exceeds the benefit of change. Many systems reach that point in some of their features or configurations.

This argument is of course absurd, but we all have worked on systems where we were afraid of changing things in fear of breaking other things, haven't we? 

> This challenge is doubly important if you are a software architect. Software architects are, by virtue of their job description, more focused on the structure of the system than on its features and functions. Architects create an architecture that allows those features and functions to be easily developed, easily modified, and easily extended.
> 
> Just remember: If architecture comes last, then the system will become ever more costly to develop, and eventually change will become practically impossible for part or all of the system. If that is allowed to happen, it means the software development team did not fight hard enough for what they knew was necessary.

It is your responsibility as a software engineer to fight for the architecture. You have to fight this thankless battle because otherwise in the long-run you will end up in trouble as the cost of making changes exceeds the benefits of them.


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
    