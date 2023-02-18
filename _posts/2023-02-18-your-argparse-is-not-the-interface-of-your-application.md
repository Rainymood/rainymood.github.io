---
title: "Your argparse is not the interface of your application"
date: 2023-02-18
tags:
- programming
- python
- lessons learned
- code
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2023-02-18-your-argparse-is-not-the-interface-of-your-application/thumbnail.png"
---

This is another post in the series [lessons learned building machine learning systems]({% post_url 2022-12-21-lessons-learned-from-building-machine-learning-systems %}).

Your argparse should not be the interface of your application. Instead, your argparse should be a *specific implementation* of it. 

Consider the following example. I used to always structure my code like this

```python
import argparse
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--foo", type=int)
    args, _ = parser.parse_known_args(sys.argv[1:])
    foo = args.foo
    result = foo + 1 
```

Instead what we should do is this

```python
def run(args: argparse.Namespace):
    foo = args.foo
    result = foo + 1 

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--foo", type=int)
    args, _ = parser.parse_known_args(sys.argv[1:])
    run(args)
```

The difference is that the argparse becomes a *specific implementation* of the *actual* interface, which is the `run` function.

Before: No separation between interface (the argparse) and implementation (also the argparse).

After: Clear separation between interface (`run` function) and implementation (argparse).

This separation makes our code easier to test. 

We now can write another testing implementation just using the `run` function instead of having to rely on the argparse to test the full flow of the application.

In this trivial example it almost seems obvious, but for some reason I did manage to completely forgot this in a larger and more complex codebase. 

The solution is simple, just wrap whatever is happening in your `__main__` into a single function called `run` :)

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
    