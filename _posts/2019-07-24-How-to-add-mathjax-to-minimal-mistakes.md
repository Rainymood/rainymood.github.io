---
title: "How to add Latex to Minimal Mistakes"
date: 2019-07-24
categories:
  - blog
tags:
  - minimal-mistakes
  - Jekyll
  - update
---
<!-- ctrl + alt + v -->

In one of my
[previous](http://www.janmeppe.com/blog/how-to-change-theme-to-minimal-mistakes/)
blog posts I show you how to set up the Minimal Mistakes theme for
your Github page.
In this blog post I show how to add Latex support to your Minimal
Mistakes jekyll blog and is largely based on
[this](https://sort-care.github.io/Latex-on-Blog/).

## Step 1. Set markdown engine to kramdown

In your `_config.yml` change the engine to kramdown as follows

```yml
# Build settings
markdown: kramdown
remote_theme: mmistakes/minimal-mistakes
...
```

## Step 2. Copy over `scripts.html`

This is where stuff gets a little bit tricky. This blog was set up by
forking [this](https://github.com/mmistakes/mm-github-pages-starter)
repo and then using the original repo as a remote theme. To get Latex
support we first have to go to the original Minimal Mistakes repo
[here](https://github.com/mmistakes/minimal-mistakes) and copy over
`minimal-mistakes/_includes/scripts.html` locally to our
`_includes/scripts.html`.

## Step 3. Modify `scripts.html`

We are now going to modify `scripts.html` and **append** the following content:

```html
<script type="text/javascript" async
	src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML">
</script>

<script type="text/x-mathjax-config">
   MathJax.Hub.Config({
     extensions: ["tex2jax.js"],
     jax: ["input/TeX", "output/HTML-CSS"],
     tex2jax: {
       inlineMath: [ ['$','$'], ["\\(","\\)"] ],
       displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
       processEscapes: true
     },
     "HTML-CSS": { availableFonts: ["TeX"] }
   });
</script>
```

Note that this overrides any other include file in the remote
theme. So the contents of the original file in the remote theme will
be overwritten. This means that this fix/update is liable to break
with new updates. Be mindful of this.

## Step 4. That's it!

If you did everything properly then this should render nicely:

$$ e^{i \pi} = -1$$

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
	<label for="mce-EMAIL">Liked this article and want to hear more?</label>
	<input type="email" value="" name="EMAIL" class="email" id="mce-EMAIL" placeholder="email address" required>
    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
    <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_92fe86c389878585bc87837e8_50543deff9" tabindex="-1" value=""></div>
    <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button"></div>
    </div>
</form>
</div>

<!--End mc_embed_signup-->
