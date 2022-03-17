---
title: "How to fix AttributeError: module 'regex' has no attribute 'Match' for SQLFluff"
date: 2022-03-17
tags: tutorial sql 
categories: blog
toc: false
toc_sticky: false
header:
  teaser: "/../assets/2022-03-01-how-to-scale-up-your-code/thumbnail.png"
---

In this blog post I'll show you how to fix the `AttributeError: module 'regex' has no attribute 'Match` error when trying to install SQLFluff. 

[SQLFluff](https://www.sqlfluff.com/) is popular SQL linter and formatter. 

I installed `sqlfluff`

```bash
$ pip install sqlfluff
Collecting sqlfluff
...
Requirement already satisfied: regex in c:\users\janmeppe\anaconda3\lib\site-packages (from sqlfluff) (2021.4.4)
...
Successfully installed sqlfluff-0.11.1
```

And tried to [run the instructions](https://docs.sqlfluff.com/en/stable/gettingstarted.html), but this happened

```bash
$ echo "  SELECT a  +  b FROM tbl;  " > test.sql
$ sqlfluff lint test.sql
Traceback (most recent call last):
  ...
  File "c:\users\janmeppe\anaconda3\lib\site-packages\sqlfluff\core\templaters\slicers\tracer.py", line 389, in JinjaAnalyzer
    self, m_open: regex.Match, m_close: regex.Match, tag_contents: List[str]
AttributeError: module 'regex' has no attribute 'Match
```

This has something to do with `regex==2021.4.4` being broken. See also [this](https://www.google.com/url?q=https://github.com/psf/black/issues/2623&sa=D&source=docs&ust=1647511821565077&usg=AOvVaw3rKnin_DAvlcN0R8paIPmX) github issue. 

How I fixed it:
1. Uninstall `regex==2021.4.4`
2. Upgrade `pip`
3. Install the most recent version of `regex`

1) Uninstall `regex`

```bash
$ pip uninstall regex
Found existing installation: regex 2021.4.4
Uninstalling regex-2021.4.4:
  Would remove:
    c:\users\janmeppe\anaconda3\lib\site-packages\regex-2021.4.4.dist-info\*
    c:\users\janmeppe\anaconda3\lib\site-packages\regex\*
Proceed (y/n)? y
  Successfully uninstalled regex-2021.4.4
```

2) Upgrade `pip`

```bash
$ python -m pip install --upgrade pip
Collecting pip
  Downloading ...
     |████████████████████████████████| 2.1 MB 149 kB/s
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 21.0.1
    Uninstalling pip-21.0.1:
      Successfully uninstalled pip-21.0.1
Successfully installed pip-22.0.4
```

3) Reinstall the most recent version of `regex`

```bash
$ pip install regex
...
Installing collected packages: regex
Successfully installed regex-2022.3.15
```

Should work now

```bash
$ sqlfluff
Usage: sqlfluff [OPTIONS] COMMAND [ARGS]...

  Sqlfluff is a modular sql linter for humans.

Options:
  --version   Show the version and exit.
  -h, --help  Show this message and exit.

Commands:
  dialects  Show the current dialects available.
  fix       Fix SQL files.
  lint      Lint SQL files via passing a list of files or using stdin.
  parse     Parse SQL files and just spit out the result.
  rules     Show the current rules in use.
  version   Show the version of sqlfluff.
```

Hope this helps!

<!-- https://longqian.me/2017/02/09/github-jekyll-tag/ -->

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
