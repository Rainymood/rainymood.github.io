---
title: "Inversion of Control visualized"
date: 2023-02-04
tags:
- software architecture
- programming
- learning
- cosmicpython
- inversion of control
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2023-02-04-inversion-of-control-visualized/thumbnail.png"
---
<!-- alt + ctrl + v -->

In this blog post I visualize an important concept called **Inversion of Control**.

Blatantly stolen from [cosmicpython.com](https://www.cosmicpython.com/blog/2019-04-15-inversion-of-control.html), but I like my visualization a tiny bit more because it is more explicit about who implements what.

I want to reproduce it so I really understand it and internalize it :).

# Before

Consider the simple example of a circular dependency:

* Module `A` uses module `B` 
* Module `B` uses module `A`

These modules are *tightly coupled*. 

In fact, these modules are so tightly coupled they might as well be a single unit!

![](/../assets/2023-02-04-inversion-of-control-visualized/2023-02-04-09-11-35.png)

How do we fix this? Inversion of Control to the rescue.

# After

Now we use *Inversion of Control* to break free of this circular dependency:

* Module `A` uses `<<B>>` (which is module `B`'s interface)
* Module `B` uses/implements `<<B>>` (is a specific implementation of)
* Module `B` uses module `A`

Notice that `A` **knows nothing** about `B` (only about the interface `<<B>>`).

![](/../assets/2023-02-04-inversion-of-control-visualized/2023-02-04-09-12-11.png)


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
    