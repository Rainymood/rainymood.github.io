---
title: "How to add a teaser image to minimal mistakes"
date: 2020-04-06
categories:
  - blog
tags:
  - Jekyll
  - update
header:
  teaser: "/assets/2020-04-06-add-teaser-to-minimal-mistakes/before.png"
---

In this blog post I will show you how to add a simple teaser image to the
"You may also like" section of the [minimal
mistakes](https://mmistakes.github.io/minimal-mistakes/about/) Jekyll theme.
Adding a teaser image is super simple, but for some reason I spent way
more time on it than I would like to admit. 

## Before

<img src="/assets/2020-04-06-add-teaser-to-minimal-mistakes/before.png">

## After

<img src="/assets/2020-04-06-add-teaser-to-minimal-mistakes/after.png">

## How to add a teaser image

Adding a teaser image in minimal mistakes is easy, you just have to change
the front matter of your post by adding a header and teaser tag

<script src="https://gist.github.com/Rainymood/b8fcbfb82949a188d31ceccf95ce1819.js"></script>

<!-- ```YAML
header: 
  teaser: "/path/to/image.png"
``` -->

For example, the front matter of this post looks like this. 

<script src="https://gist.github.com/Rainymood/2b58c32c9efc7e6b329128fe6a4344f4.js"></script>

<!-- ```YAML
---
title: "How to add a teaser image to minimal mistakes"
date: 2020-04-06
categories:
  - blog
tags:
  - Jekyll
  - update
header:
  teaser: "/assets/2020-04-06-add-teaser-to-minimal-mistakes/before.png"
---
``` -->

## Conclusion

Adding teaser images in minimal mistakes is deceptively simple, you just need
to know what to change. For some reason I was not able to figure it out and
had to ask someone myself.

With this short and simple blog post I hope to help someone with the same
burning question as me: "How do I add teaser images to minimal mistakes?"

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