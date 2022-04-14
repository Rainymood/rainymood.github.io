---
title: "How to structure your python code"
date: 2022-04-05
tags:
  - tutorial
  - python
categories: blog
toc: false
toc_sticky: false
header:
  teaser: "/../assets/2022-04-05-basic-setup/thumbnail.png"
---

In this post I want to show you how you can set up and structure your python code if you don't know where to start. Just copy our setup!

This is actually how we lay out most of our python projects here at [Snappet](https://us.snappet.org/) (We're [hiring](https://snappet.recruitee.com/)!).

I made a small repository that is fully functional (you can build the docker, run the code, etc.) that shows how we structure our code.

View the repository on Github [here](https://github.com/Rainymood/basic-setup).
{: .notice--success}

What I really like about this setup:

* **Conda + Poetry for environment and package management** For our environment and package management we use a combination of [Conda](https://docs.conda.io/en/latest/) and [Poetry](https://python-poetry.org/). We have a separate virtual environment for all our projects each with their own `pyproject.toml`.
* **Clear separation of the interface/entrypoint and the code** This setup clearly separates the interface of the code (in the `entrypoints/` folder) from the source code (in the `src/` folder). If you don't know the project at all you should, in theory, be able to run everything by just fiddling with the entrypoint knobs.
* **Containerisation using docker.** This setup (thanks to poetry) also allows us to install the source folder as a package which makes it easy to dockerize, yet, at the same time we can run it locally using the entrypoint too. The docker just installs the package and calls the entrypoint.

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
  <label for="mce-EMAIL">Liked this article and want to hear more? Join 40+ others and subscribe!</label>
  <input type="email" value="" name="EMAIL" class="email" id="mce-EMAIL" placeholder="email address" required>
    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
    <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_92fe86c389878585bc87837e8_50543deff9" tabindex="-1" value=""></div>
    <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button"></div>
    </div>
</form>
</div>
<!--End mc_embed_signup-->
