---
title: "How to add a new kernel to your Jupyter Notebook" 
date: 2020-08-20
categories:
  - blog
tags:
  - blog
  - python
  - data-science
header:
  teaser: "/assets/2020-08-20-how-to-add-new-kernel-in-jupyter-notebook/teaser-1280x700.jpeg"
---

In this blog post, I'll tell you how to add a new kernel to your Jupyter notebook
in just 3 simple steps.

## Step 1: Install virtualenvwrapper

<img src="/assets/2020-08-20-how-to-add-new-kernel-in-jupyter-notebook/img3.png">

Follow [this](https://virtualenvwrapper.readthedocs.io/en/latest/) link and
install **virtualenvwrapper**. Virtualenvwrapper is an extension to
virtualenv, which provides additional commands to manage your virtual
environments. Make sure you install it in your `PATH` by following the
instructions. 

To verify your installation, use `workon`. This lists your current virtualenvs
installed with virtualenvwrapper, and should return nothing.

```bash
$ workon
tmp
```

I have one virtualenv, `tmp`, installed with virtualenvwrapper. 

## Step 2: Create a new virtualenv called data-science

Create a new virtualenv with `mkvirtualenv`.

```bash
$ mkvirtualenv data-science
```

Your terminal should now have a `data-science` prompt in front of it. This
indicates that you are in the `data-science` virtual environment.

```bash
(data-science) $ echo "Hi"
Hi
```

To exit the virtualenv use `deactivate`

```bash
(data-science) $ deactivate
$ ... 
```

To work on your virtualenv use `workon`

```bash
$ workon data-science
(data-science) $ ...
```

## Step 3: Add the kernel to you jupyter notebook

Finally, **while you are still in your virtualenv** `data-science`, add your
kernel to your jupyter notebook with the following command.

```bash
(data-science) $ ipython kernel install --name “data-science” --user
```

Once this step is complete, your new kernel will appear in your jupyter
notebooks! Note that you **do not have to be in the virtualenv to access the
new kernel**.

<img src="/assets/2020-08-20-how-to-add-new-kernel-in-jupyter-notebook/img2.png">

## Conclusion

And that's how you add a new kernel in your jupyter notebook in 3 simple
steps. 

For the really lazy people who just want to copy paste something and
slam it in their terminal, this one is for you.

```bash
mkvirtualenv data-science
workon data-science
ipython kernel install --name “data-science” --user
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
  <label for="mce-EMAIL">Liked this article and want to hear more? Join 53 others and subscribe!</label>
  <input type="email" value="" name="EMAIL" class="email" id="mce-EMAIL" placeholder="email address" required>
    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
    <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_92fe86c389878585bc87837e8_50543deff9" tabindex="-1" value=""></div>
    <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button"></div>
    </div>
</form>
</div>
<!--End mc_embed_signup-->