---
title: "Docker optimization trick: install your dependencies first and your code second"
date: 2022-03-25
tags:
  - tutorial
  - docker
categories: blog
toc: false
toc_sticky: false
header:
  teaser: "/../assets/2022-03-17-docker-optimisation/thumbnail.png"
---

Is your docker build step slow? Assuming you can install your code as a package,
try installing your dependencies first and your code second. 

If you install your code and dependencies together any change in the code will
result in an invalidation of the cache. This means that Docker is going to do
the dependency steps all over again.

Splitting them up fixes this, hopefully making your docker builds much faster by leveraging the cache.

```docker
WORKDIR "/opt"

# Copy *only* package information to prevent code changes from killing the cache
COPY poetry.lock /opt/poetry.lock
COPY pyproject.toml /opt/pyproject.toml

# Install the packages
RUN \
  pip install poetry && \
  poetry install --no-root

# Copy code 
COPY src/ /opt/src/

# Install module
RUN \
  pip install . --no-dependencies && \
  python -c "import ..."
``` 

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
