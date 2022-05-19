---
title: "How to change the font size of the code blocks in minimal mistakes using Github pages"
date: 2022-05-18
tags:
  - blog
  - jekyll
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2022-05-18-how-to-change-code-blocks-minimal-mistakes/thumbnail.png"
---

In this blog post I want to share with you how to change the font size of the code blocks in the [minimal mistakes]() Jekyll theme **when using Github Pages**.

I'll show you how to change the styling of these code blocks:

```python
def hello_world(s: str) -> None:
    ...
```

This blog post is *specifically* for [Github Pages](https://pages.github.com/), because if you search for ["how to change code block minimal mistakes theme"](https://www.google.com/search?q=how+to+change+code+block+minimal+mistakes+theme&oq=how+to+change+code+block+minimal+mistakes+theme&aqs=edge..69i57j69i64.13054j0j4&sourceid=chrome&ie=UTF-8) you find [this](https://mmistakes.github.io/minimal-mistakes/markup-syntax-highlighting/) and [this](https://www.cross-validated.com/Personal-website-with-Minimal-Mistakes-Jekyll-Theme-HOWTO-Part-II/) page, but these don't use Github Pages!


## Step 1. Overwrite the default settings in `main.scss`

To change the styling of the code box you need to overwrite the default settings
in `assets/css/main.scss`. So create that file if it doesn't exist. 

## Step 2. Add styling to the  `highlight` class

Then, you want to add styling to the `highlight` class, which is the code box. This is a stripped down version of my `main.scss` that shows the styling applied (find the full version [here](https://github.com/Rainymood/rainymood.github.io/blob/master/assets/css/main.scss)):

```scss
---
# Only the main Sass file needs front matter (the dashes are enough)
---

@charset "utf-8";

// ... stuff

@import "minimal-mistakes";

// This changes the code box
.highlight {
  margin: 0;
  padding: 0.5em;
  font-family: $monospace;
  font-size: $type-size-5b;
  line-height: 1.8;
}
```

How did I know to style this exactly this `highlight`class? 

Good question. To figure this out (and it took me a while) you can enter the
inspection mode in your web browser and mouseover the code block. You see that
some html with `<div class="highlight"></div>` gets selected and that's how you
know.

![](/../assets/2022-05-18-how-to-change-code-blocks-minimal-mistakes/2022-05-18-17-06-37.png)

Hope this helps!


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
