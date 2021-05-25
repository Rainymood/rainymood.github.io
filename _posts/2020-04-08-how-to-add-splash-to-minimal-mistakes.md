---
title: "How to add a splash image to minimal mistakes" 
date: 2020-04-08
categories:
  - blog
tags:
  - minimal-mistakes
  - Jekyll
  - update
header:
  teaser: "/assets/2020-04-08-how-to-add-splash/splash1.png"
---

In this blog post I will show you how to add a simple splash image to your
minimal mistakes blog. View my current splash page
[here](http://janmeppe.com/splash-page).

We start with the most simple splash page and slowly add more and more
elements. This tutorial is an extension of the excellent official
documentation
[here](https://mmistakes.github.io/minimal-mistakes/docs/layouts/).

## Add splash image and call to action

The splash page will look something like this.

<img src="/assets/2020-04-08-how-to-add-splash/splash1.png">

* Create a new page `_pages/splash-page.md`
* Download [this picture](https://unsplash.com/photos/-2j6VAaHNvA) and save it as `assets/splash/coffee.jpg`
* Add the following front matter YAML to `_pages/splash-page.md`

```YAML
---
title: "Splash Page"
layout: splash
permalink: /splash-page/
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /assets/splash/coffee.jpeg
  actions:
    - label: "Download"
      url: "#test-link"
excerpt: "Bacon ipsum dolor sit amet salami ham hock ham, hamburger corned beef short ribs kielbasa biltong t-bone drumstick tri-tip tail sirloin pork chop."
---
```

## Add some intro text

Adding some intro text is easy and looks like this. 

<img src="/assets/2020-04-08-how-to-add-splash/splash2.png">

To get this result add this to your front matter YAML. 

```YAML
intro: 
  - excerpt: 'Nullam suscipit et nam, tellus velit pellentesque at malesuada, enim eaque. Quis nulla, netus tempor in diam gravida tincidunt, *proin faucibus* voluptate felis id sollicitudin. Centered with `type="center"`'
```

And this to the body of your post.

```
{% raw %}{% include feature_row id="intro" type="center" %}{% endraw %}
```

## Add a feature row with 3 images

Adding a feature row with three images is easy. 

<img src="/assets/2020-04-08-how-to-add-splash/splash3.png">

Save three images to `/assets/splash/` (I named them `feat1-1.jpg`, `feat1-2.jpg`, and `feat1-3.jpg`). What we are going to do is to define a `feature_row` in the front matter and give the following attributes: 

* `image_path`
* `title`
* `excerpt`
* `url`
* `btn-label`
* `btn-class`

So add this to your front matter. 

```YAML
feature_row:
  - image_path: /assets/splash/feat1-1.jpg
    title: "Placeholder 1"
    excerpt: "Sample text 1 with **markdown** formatting."
    url: "#test-link"
    btn_label: "Read More"
    btn_class: "btn--primary"
  - image_path: /assets/splash/feat1-2.jpg
    title: "Placeholder 2"
    excerpt: "This is some sample content that goes here with **Markdown** formatting."
    url: "#test-link"
    btn_label: "Read More"
    btn_class: "btn--secondar"
  - image_path: /assets/splash/feat1-3.jpg
    title: "Placeholder 3"
    excerpt: "This is some sample content that goes here with **Markdown** formatting."
    url: "#test-link"
    btn_label: "Read More"
    btn_class: "btn--primary"
```

And include this feature row in your the body of your page.

```
{% raw %}{% include feature_row %}{% endraw %}
```

## Add a left aligned image 

Let's add a left-aligned image. 

<img src="/assets/2020-04-08-how-to-add-splash/splash4-left.png">

We can repeat this trick create a new `feature_row_left`

```YAML
feature_row_left:
  - image_path: /assets/splash/feat1-1.jpg
    title: "Left aligned placeholder 1"
    excerpt: "Left-aligned image centered with"
    url: "#test-link"
    btn_label: "Read More"
    btn_class: "btn--primary"
```

And add another `feature_row` but with another `id` and `type`!

```
{% raw %}{% include feature_row id="feature_row_left" type="left" %}{% endraw %}
```


## Add a right aligned image

This is supposed to work for a right aligned image too. Add this to your
front matter YAML of your `splash-page.md` 

```YAML
feature_row_right:
  - image_path: /assets/splash/feat1-2.jpg
    title: "Placeholder 1"
    excerpt: "Right-aligned image with ``"
    url: "#test-link"
    btn_label: "Read More"
    btn_class: "btn--primary"
```

Add this in the body of your `splash-page.md`

```
{% raw %}{% include feature_row id="feature_row_right" type="right" %}{% endraw %}
```

Which, for some reason, doesn't work for me. For me even though we add
`type=right` it aligns to the center. 

<img src="/assets/2020-04-08-how-to-add-splash/splash5-right.png">

## Conclusion

The complete front matter can be found
[here](https://gist.github.com/Rainymood/35ae7d900f4d8a3d3199ee20fefe2567#file-splash-page-md)
as a gist.

Adding a splash image in minimal mistakes is easy if you know how to do it.
We create a new page `_pages/splash-page.md` and populate it with some front
matter. We make use of the
[feature_row](https://github.com/mmistakes/minimal-mistakes/blob/master/docs/_docs/14-helpers.md)
helper function and use templates to dynamically link images. That's it! For
some reason I could not get the right-aligned image to work, but hopefully
you still learned something!

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