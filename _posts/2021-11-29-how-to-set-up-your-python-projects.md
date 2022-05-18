---
title: "How to set up your Python projects with conda and poetry"
date: 2021-11-29
categories:
  - blog
  - python
toc: false
toc_sticky: false
tags:
  - update
  - python
header:
  teaser: "/../assets/2021-11-29-how-to-set-up-your-python-projects/thumbnail.png"
---

At my current job we use [conda](https://docs.conda.io/en/latest/) to manage our
environments and [poetry](https://python-poetry.org/docs/) to manage our packages. I 
have to say that the setup is pretty sweet and wanted to share it with you guys.

Imagine that we are working on a generic project called `project-name` then the 
setup is as follows

```bash
conda create --name project-name  python=3.7
conda activate project-name
pip install poetry
poetry config virtualenvs.create false
poetry install --no-root
ipython kernel install --name "project-name" --user
```

This initialises a `conda` environment with a name and the correct python version, 
installs `poetry` using pip, and then installs and manages your packages through 
`poetry`, finally it installs a jupyter kernel with the same name. 

Just change `project-name` to the name of your repo and you're all set!

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
