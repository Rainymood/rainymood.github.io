---
title: "How to change Jekyll theme to Minimal Mistakes"
date: 2019-07-16
categories:
  - blog
tags:
  - Jekyll
  - update
header:
  - teaser: "/assets/2019-06-16-how-to-change-theme-to-minimal-mistakes/teaser.jpg"
---

Recently I migrated my whole blog from the Cayman theme to the Minimal Mistakes theme, which can be found [here](https://mmistakes.github.io/minimal-mistakes/). This blog post explains how to quickly get up and running with the Minimal Mistakes theme.

**Before**

<img src="/assets/2019-06-16-how-to-change-theme-to-minimal-mistakes/blog-cayman-theme.jpg">

**After**

<img src="/assets/2019-06-16-how-to-change-theme-to-minimal-mistakes/blog-minimal-mistakes-theme.jpg">

Setting this is up is ridiculously simple if you know what you're doing. I am making this blog post because I want to save people the headache of spending a whole day debugging something they don't actually have to because they followed the wrong instructions.

This post assumes that you are going to run your blog using [Github pages](https://pages.github.com). Note that you can only have 1 Github pages repo that points towards `<username>github.io`, all other Github pages are going to point towards `<username>github.io/<repo-name>`.

## Step 1. Fork the minimal-mistakes starter repo

Go to the Minimal Mistakes Github pages starter [found here](https://github.com/mmistakes/mm-github-pages-starter) and fork the repo.

<img src="/assets/2019-06-16-how-to-change-theme-to-minimal-mistakes/001-fork.jpg">

## Step 2. Change the repo name

Click on `settings` and change the repository name. I chose to rename the repo to `minimal-mistakes`.

**Option 1** If you rename the repo to `<username>.github.io` then your Github pages will be hosted on `<username>.github.io`. For me this becomes `rainymood.github.io` which can be found [here](https://rainymood.github.io).

**Option 2** If you rename it to anything else, say `minimal-mistakes`, then your Github pages will be hosted on `<username>.github.io/<repo-name>`. For me this becomes `rainymood.github.io/minimal-mistakes` which can be found [here](https://rainymood.github.io/minimal-mistakes).

<img src="/assets/2019-06-16-how-to-change-theme-to-minimal-mistakes/002-edit.jpg">

## Step 3. That's it!

**It's that simple.**

Don't be like me and waste a full day debugging something you don't actually have to. Just fork the repo and start publishing!

This is what the final product looks like and you can find it [here](https://rainymood.github.io/minimal-mistakes).

<img src="/assets/2019-06-16-how-to-change-theme-to-minimal-mistakes/003-done.jpg">



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
