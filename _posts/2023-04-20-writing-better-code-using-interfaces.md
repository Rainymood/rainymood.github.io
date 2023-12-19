---
title: "Writing better code using interfaces"
date: 2023-04-20
tags:
- architecture
- programming
- python
- lessons learned
- cosmicpython
- inversion of control
- code
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2023-04-20-writing-better-code-using-interfaces/thumbnail.png"
---
<!-- ctrl + alt + v -->

One thing that I've learned recently and that has improved my coding significantly is writing code in terms of interfaces. 

The famous [dependency injection](https://en.wikipedia.org/wiki/Dependency_injection#:~:text=In%20software%20engineering%2C%20dependency%20injection,leading%20to%20loosely%20coupled%20programs.) mantra states that you should: *"depend on abstractions and not on implementations"*. 

If you don't understand the underlying idea behind this mantra, then the statement itself is so vague and general that it is practically useless.

I want to give a nice example illustrating the idea underlying this mantra so that you have a better understanding of the underlying concept. Then, once you understand that, the mantra becomes incredibly powerful on its own.

For me, the main idea behind all this talk about interfaces boils down to the fact that you want to **design for swappability**.
Design your code in such a way that the things that you *want to swap out, are easy to swap out*.

I'm going to lean into the [functional core imperative shell](https://www.destroyallsoftware.com/screencasts/catalog/functional-core-imperative-shell) idea here a bit. Your code can be thought of as an onion with two layers:

1.  The first layer we call the shell. For now, just think of it as the place where all data io happens
2.  The second layer we call the core is where all your core business logic happens, ideally this core is completely isolated from the outside world

![](/../assets/2023-04-20-writing-better-code-using-interfaces/2023-04-20-18-33-58.png)

Imagine that, for some reason, we need to make a ping to AWS. We do not really want our core domain logic, the second layer, to be polluted with these external system calls. 

How do we solve this? 

By putting it on the outside of our program, by putting it in the shell so we can swap it out! Remember that we want to design for swappability.

![](/../assets/2023-04-20-writing-better-code-using-interfaces/2023-04-20-18-37-13.png)

When in production we need to be able to ping AWS. But during testing we should be able to swap out this service. We want to swap it out with a fake AWS that we control, for testing.

![](/../assets/2023-04-20-writing-better-code-using-interfaces/2023-04-20-18-39-10.png)

But this is pretty hard. How do we do this? 

With interfaces!

This is exactly what is meant by *depending on abstractions and not on implementations*. Let me show you how.

Imagine that we are now on the inside of our core and we want to make a call to the AWS service. To do this, we define an *interface* that we call.

![](/../assets/2023-04-20-writing-better-code-using-interfaces/2023-04-20-18-42-48.png)

This means that we specify an interface, in this case the `AwsServiceInterface`. All that this does is that it tells us which functions we can call. Any *implementation* of this interface *must* at least implement the interface.

The real AWS *implementation* (not the interface!) calls a real `boto` function and hits production s3 like so:


![](/../assets/2023-04-20-writing-better-code-using-interfaces/2023-04-20-18-45-34.png)

The fake that we use for testing, on the other hand, always returns 200 (or could hit some fake local setup).

![](/../assets/2023-04-20-writing-better-code-using-interfaces/2023-04-20-18-46-56.png)

It really took me a while to get this but the beauty of this now is that grey, the core of our program, does not know *anything* about the outside world. 

![](/../assets/2023-04-20-writing-better-code-using-interfaces/2023-04-20-18-51-45.png)


All that it knows is the interface that is implemented, `AwsServiceInterface` and the functions defined in the interface.

Now you should be able to understand it a bit better when people say profound things like: *"depend on abstractions and not on implementations"*. You can say "mmm mmmm" and mumble in agreement because you are enlightened too now. 

Just because I enjoy talking about this so much, let me repeat myself. We now know what we mean by **talking in terms of interfaces**. We now depend on an abstraction (the interface, green) instead of the implementation (real or fake implementation, yellow/orange).

**Remember** Depend on abstractions, not implementations
{: .notice--success}

[1] The final picture is not completely accurate, but you get the point, at test time we use the one, at run time we use the other


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
    