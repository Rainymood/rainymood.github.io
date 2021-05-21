---
title: "How to paste a screenshot from your clipboard in VScode (and how this improved my writing workflow)"
date: 2021-05-28
categories:
  - blog
tags:
  - blog
  - workflow
  - automation
header:
  teaser: "/assets/2020-09-02-paste-image/teaser.png"
---

In this blog post I want to tell you how I **significantly sped up my writing workflow** by hacking together a feature that allows me to seamlessly paste images from my clipboard in VScode. 

I started writing this blog post more than a year ago (2020-09-02) but left it
in my drafts folder and only decided to publish it today (2021-05-28). I have to
say, this was one heck of a fix and I've been happily using it since. This was
very high leverage: small change, big impact.
{: .notice--success}

For some context, this blog is a static [Jekyll](https://jekyllrb.com/) blog using the [minimal
mistakes](https://mmistakes.github.io/minimal-mistakes/) theme. I write the blog posts in `.md` files using VScode. 

I really hated writing blog posts before this fix because adding images was a
hassle. I had to grab the image, put it in the right folder, get the path, paste
the path, aaahhhh! I get frustrated again just by thinking about it. At some
point I said to myself, this is enough, let's fix this. So I did. 

## How to add a screenshot (before and after)

I like to have a lot of images in my blog posts because I think they make them
more engaging.  This is what my workflow for pasting images in my blog posts
looked like before and after.

Before: 

* Make screenshot (f4)
* Open Finder
* Go to Downloads
* Copy screenshot
* Make new tab in finder
* Go to correct blog image directory
* Create new directory if it doesn't exist
* Paste image
* Copy relative path
* Paste in blog post
* Fix formatting

After: 

* Make screenshot (f4)
* Paste (cmd + alt + v)

![](/../assets/2020-09-02-paste-image/2020-09-02-11-44-40.png)

WOAH! That's pretty cool isn't it? 

I wrote this post with my new workflow and it feels *really really good*.
Seamlessly pasting images without any friction makes writing much more enjoyable.

## How to seamlessly paste images in VScode

Download and install the [Paste Image](https://marketplace.visualstudio.com/items?itemName=mushan.vscode-paste-image) extension. 

![](/../assets/2020-09-02-paste-image/2020-09-02-11-21-52.png)

Click on the gear icon to open up the settings.

![](/../assets/2020-09-02-paste-image/2020-09-02-11-27-28.png)

Change the settings to have the following **Paste Image: Path** and **Paste Image: Prefix**. 

![](/../assets/2020-09-02-paste-image/2020-09-02-11-28-34.png)

And there you go! Now you can seamlessly paste images using `cmd + alt + v`!

## Why this works

These settings work because the folder structure of this blog is like this:

* rainymood.github.io/
    * _posts/
        * 2020-09-02-blog-post.md
    * assets/
        * 2020-09-02-blog-post/
            * Image1.png
            * Image2.png

The `/_posts` directory stores my blog posts which are simple markdown (`.md`) files. 

The `/assets` directory stores the images in a folder with the same name as the blog post, but without the extension.

We want to put the pasted image in `${projectRoot}/assets/${currentFileNamewithoutExt}`. 

For some reason Jekyll needs a single forward slash (`/`) in front of the path to make it work, hence the prefix. 

# Conclusion

That's it!

It's a simple fix and took me an hour to figure this out, but because I write so
much I'm sure it will prove itself valuable in the long run. I am kind of
annoyed at myself for not fixing this sooner. I'm thinking about all the time I
wasted trying to fix the formatting... oh well!

Every once in a while, take a step back and critically assess your whole
workflow. What parts are you annoyed at and what parts can you automate away for
yourself?

---

Big shoutout to Mushan and his [extension](https://marketplace.visualstudio.com/items?itemName=mushan.vscode-paste-image).


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
  <label for="mce-EMAIL">Liked this article and want to hear more? Join >40 others and subscribe!</label>
  <input type="email" value="" name="EMAIL" class="email" id="mce-EMAIL" placeholder="email address" required>
    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
    <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_92fe86c389878585bc87837e8_50543deff9" tabindex="-1" value=""></div>
    <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button"></div>
    </div>
</form>
</div>
<!--End mc_embed_signup-->