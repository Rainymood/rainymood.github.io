---
title: "A Beginner's Guide to Domain-Driven Design Boiled Down to One Image"
date: 2024-11-15
tags:
# Blog or how-to
- blog

# Work or personal?
- work

# Start here themes
- systems
- software
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2024-11-15-a-beginners-guide-to-domain-driven-design-boiled-down-to-one-image/thumbnail.png"
---

![](/../assets/2024-11-15-a-beginners-guide-to-domain-driven-design-boiled-down-to-one-image/2024-11-15-16-04-31.png)

[Domain-Driven Design (DDD)](https://martinfowler.com/bliki/DomainDrivenDesign.html) is a tough beast to understand, but the core concepts behind it I think are remarkably simple and will make you write better code, and this image symbolizes its core concept to me.

That core concept is the following: **Can you solve your problem in your domain space?**

DDD makes a clear distinction between things that are on the outside of your domain (real nitty gritty things like the files and database icons pointing inwards) and things that are inside of your domain space (core).

This domain space we call the core is in essence an abstract world. This is a clean and pristine world. This core should not have to worry about real world details such as file formats and databases and persistence. This core should be an abstract world filled with abstract concepts in which you can solve your problem.

The question then becomes: Can you solve your problem in this world free of the details and restrictions of the "real" world?

If yes, then the rest of the process becomes straightforward:
1. Translate external real-world elements into domain objects
2. Solve the problem using these domain objects in the core
3. Translate back these domain objects into real-world nitty gritty items.

That's it. That is the core of Domain-Driven Design: Can you solve your problem in your domain space (core)?

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
    