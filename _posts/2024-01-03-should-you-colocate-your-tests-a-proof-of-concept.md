---
title: "Should you colocate your tests? A proof-of-concept"
date: 2024-01-03
tags:
# Blog or how-to
- blog

# Work or personal?
- work

# Big themes that I write about
- engineering
- testing

# Programming languages
- golang
- python
- programming
- code
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2024-01-03-should-you-colocate-your-tests-a-proof-of-concept/thumbnail.png"
---
<!-- ctrl + alt + v -->

<!-- Checklist:
Title = insight
Interesting 1st sentence
Short and concise -->

<!-- 1. interesting hook -->
I've been writing a lot of golang recently and there is one big thing that golang gets right over python: it colocates source and test code.

Colocating source and test code means putting them next to each other. So instead of having a separate `src` and `test` directory, you have `main.go` and `main_test.go`. If try this in python this is what it would look like: 

![](/../assets/2024-01-03-should-you-colocate-your-tests-a-proof-of-concept/2024-01-03-20-54-57.png)

Colocating has many benefits and drawbacks, but I think there is one big pro that outweighs all the other cons. 

**Colocating your source and test code elevates your test code to the same importance as your source code**. 

Too often I've seen projects where testing is an afterthought, but it shouldn't be! I believe that your tests are as important as your source code because they are the only verifiable source of truth for the behavior of your program. (See also the [Github](https://github.com/Rainymood/colocated-tests) repo for more information)

You probably agree with me quite quickly that this is nice for unit tests, but what about integration tests I hear you think? Good question. I haven't figured this out myself completely but someone on Reddit said this:

> Rust does both. The rust book suggests unit tests within the source files (in separate modules) and integration tests in the test directory. I've found it makes simple unit and property tests very convenient (I usually use hspec with Haskell). However, it means cargo can't differentiate between imports for the library vs the test suite.

Anyway, I made a small proof of concept (POC) to explore this idea further and I wanted to share it. I wonder if this leads to higher quality projects and if this approach scales to bigger projects.

Find the code on Github here: [https://github.com/Rainymood/colocated-tests](https://github.com/Rainymood/colocated-tests)

<!-- ![](/../assets/2024-01-03-should-you-colocate-your-tests-a-proof-of-concept/2024-01-04-08-39-51.png) -->

<!-- ![](/../assets/2024-01-03-should-you-colocate-your-tests-a-proof-of-concept/2024-01-04-14-53-39.png) -->


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
    