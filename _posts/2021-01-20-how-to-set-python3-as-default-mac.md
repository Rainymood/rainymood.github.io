---
title: "Set Python 3 as default on Mac"
date: 2021-01-20
categories:
  - blog
tags:
  - python
  - tool
header:
  teaser: "/../assets/2021-01-20-how-to-set-python3-as-default-mac/2021-01-20-17-43-24.png"
---


The default Python version that ships with (older) Mac OS software is
hilariously old. Because I am still developing on a mid-2014 MBP Retina (SUE ME!) I was still rocking this bad boy. But at some point I was cracking my head on Python environments and well, I just had to fix it. So here goes!

There is a right way and wrong way to set Python 3 as the default on your
Mac. I'll show you the right way. In general you *never ever* want to fuck
with your system version of Python. This is very dangerous and can mess up
many things.

To manage our global python version we will use `pyenv` and then make our shell always use `pyenv`. I will merely set the global default to Python `3.9.0` but you could also manage more version at the same time. 

## 1. Install pyenv

Install `pyenv`.


```bash
$ brew install pyenv
==> Upgrading 1 outdated package:
pyenv 1.2.10 -> 1.2.21
...
```

Validate whether you installed `pyenv` correctly.

```bash
$ pyenv -v
pyenv 1.2.21
```

## 2. Install Python

Install the desired Python version. In my case this is version `3.9.0`.

```bash
$ pyenv install 3.9.0
python-build: use openssl 1.0 from homebrew
python-build: use readline from homebrew
```

This. Will. Take. A. While. Go grab a cup of coffee or something.

## 3. Set as default

Set your installed version as the default.

```bash
$ pyenv global 3.9.0
```

Validate whether it worked.

```bash
$ pyenv version
3.9.0 (set by /Users/janmeppe/.pyenv/version)
```

## 4. Make your shell runs pyenv

Add this to your `.bash_profile` or `.zshrc`.

```bash
if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
fi
```

## Success

Great job! That's it. 

If you now run `python` you'll see that it runs `3.9.0` instead of `2.7.x`.

```bash
$ python
Python 3.9.0 (default, Jan 20 2021, 16:49:23)
[Clang 10.0.1 (clang-1001.0.46.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

## Resources

* [This tutorial on www.opensource.com](https://opensource.com/article/19/5/python-3-default-mac)

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