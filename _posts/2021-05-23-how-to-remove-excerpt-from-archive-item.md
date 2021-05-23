---
title: "How to remove the excerpt from recent posts in a minimal mistakes blog" 
date: 2021-05-21
categories:
  - blog
toc: false
toc_sticky: false
tags:
  - blog
  - minimal-mistakes
header:
  teaser: "/../assets/2021-05-23-how-to-remove-excerpt-from-archive-item/thumbnail.png"
---

In this blog post I'll show you how to remove the excerpt from your recent posts overview in your Jekyll blog running the [Minimal Mistakes theme](https://mmistakes.github.io/minimal-mistakes/) using Github pages. This blog post is only relevant if you deploy your website through [Github pages](https://pages.github.com/). If you run the minimal mistakes theme directly, simply edit the `_includes/archive-single.html` file. 

Before

![](/../assets/2021-05-23-how-to-remove-excerpt-from-archive-item/before.png)

After

![](/../assets/2021-05-23-how-to-remove-excerpt-from-archive-item/after.png)

Go to [this link](https://github.com/mmistakes/minimal-mistakes/blob/master/_includes/archive-single.html).

Download `_includes/archive-single.html` and put it in your own blog's `_includes/archive_single.html`. (For me that is `~/rainymood.github.io/_includes/archive_single.html`.)

Note that, when you do this, you are overwriting the default theme settings, so you won't get any theme updates for that particular file.

Finally, remove this line:

```html
{% raw %}
{% if post.excerpt %}<p class="archive__item-excerpt" itemprop="description">{{ post.excerpt | markdownify | strip_html | truncate: 160 }}</p>{% endif %}
{% endraw %}
```

That's it! 

---

Thanks to [this post](https://www.jasongaylord.com/blog/2020/05/31/displaying-liquid-templates-in-jekyll-code-blocks) on how to display Jekyll templates in code blocks.

See also [this github issue](https://github.com/mmistakes/minimal-mistakes/issues/2070) where the author explains it himself.

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
  <label for="mce-EMAIL">Liked this article and want to hear more? Join 53 others and subscribe!</label>
  <input type="email" value="" name="EMAIL" class="email" id="mce-EMAIL" placeholder="email address" required>
    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
    <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_92fe86c389878585bc87837e8_50543deff9" tabindex="-1" value=""></div>
    <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button"></div>
    </div>
</form>
</div>
<!--End mc_embed_signup-->
