---
title: "Rust colocates unit tests"
date: 2024-01-13
tags:
# Blog or how-to
- blog

# Work or personal?
- work

# Big themes that I write about
- engineering
# Programming languages/Cloud
- rust
- testing

categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2024-01-13-rust-colocates-unit-tests/thumbnail.png"
---
<!-- ctrl + alt + v -->

<!-- Checklist:
Title = insight
Interesting 1st sentence
Short and concise -->

<!-- 1. interesting hook -->
I’m more and more convinced that Python developers should steal this great convention from Rust developers.

I talked briefly about colocating source code and test code in [this previous blog post]({% post_url 2024-01-03-should-you-colocate-your-tests-a-proof-of-concept %}) and in that blog post I mentioned someone on Reddit who mentioned Rust. Coincidentally, it just so happens that I’ve been reading up a bit about Rust and I found the [official documentation](https://doc.rust-lang.org/book/ch11-03-test-organization.html#test-organization) talking about this and this is what they write.

Under the header **Unit Tests** the book writes:

> The purpose of unit tests is to test each unit of code in isolation from the rest of the code to quickly pinpoint where code is and isn’t working as expected. You’ll put unit tests in the src directory in each file with the code that they’re testing. The convention is to create a module named tests in each file to contain the test functions and to annotate the module with cfg(test). 

Under the header **Integration Tests** the book writes:

> In Rust, integration tests are entirely external to your library. They use your library in the same way any other code would, which means they can only call functions that are part of your library’s public API. Their purpose is to test whether many parts of your library work together correctly. Units of code that work correctly on their own could have problems when integrated, so test coverage of the integrated code is important as well. To create integration tests, you first need a tests directory.

In summary, colocate the unit tests and source code and act like integration tests are tests external to your library and hence they should stay in a separate tests directory.

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
    