---
title: "The Magic Secrets of System Design"
date: 2025-09-05
tags:
# Blog or how-to
- blog
- work
# Start here themes
- systems
- software
- complexity
- software architecture
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2025-09-05-the-magic-secrets-of-system-design/thumbnail.png"
---
<!-- ctrl + alt + v -->
<!-- cmd + alt + v -->

https://app.bannerbear.com/projects/POobgvMNDkxzxAYW70/templates/3g8zka5Y2OlaDEJXBY

https://www.photopea.com/

I return time and time and time again to John Oosterhout's timeless advice.

Magic secrets:
* **Problem decomposition**: Can we break up the system into modules or subproblems that can be solved relatively independently?
- **Working code is not enough, we must minimize system complexity**. Complexity is caused by obscurity and dependencies. Test-Driven Design (TDD) does not guarantee good design over time.
- **Classes/modules/interfaces should be deep**. Imagine a class as a rectangle. The total area is the benefit and the interface is the top side. Maximize the surface area given the smallest possible working interface. For example, UNIX file IO hides thousands of lines of code with 5 interface methods (open, close, read, write, lseek)
- **Define errors out of existence**. Defining errors out of existence means changing the semantics to make the normal case handle do everything. This reduces system complexity. For example, Java.substring should return the intersection of your array and the bounds, not throw an exception. Unset in TCL should make a variable not exist (see, changing the semantics!). Only throw an error when you really can not carry out the contract.

From: https://www.youtube.com/watch?v=bmSAYlu0NcY


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
    