---
title: "How to see log messages while unit testing in pycharm"
date: 2021-12-03
categories:
  - blog
  - python
  - testing
toc: false
toc_sticky: false
tags:
  - update
  - python
header:
  teaser: "/../assets/2021-12-03-how-to-add-logging-to-pycharm-tests/thumbnail.png"
---
  
In [this](https://stackoverflow.com/questions/24470062/how-can-i-see-log-messages-when
-unit-testing-in-pycharm) stackoverflow question someone asks how to view logging 
messages while unit testing. It got a lot of responses but none of them worked for me.

This is what worked for me to get my logs to show when testing in pycharm. 

1. Use [poetry](https://python-poetry.org/docs/cli/) for your package management
2. Add this to your `pyproject.toml`

```toml
[tool.pytest.ini_options]
log_cli = true
log_cli_level = "INFO"
log_cli_format = "%(asctime)s [%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)"
log_cli_date_format = "%Y-%m-%d %H:%M:%S"
```

Then the logs will show up when you hit run/debug in pycharm

```bash
Connected to pydev debugger (build 212.4746.96)
Launching pytest with arguments integration/test_preprocessing.py::TestPreprocessingFlow
============================= test session starts =============================
collecting ... collected 1 item
integration\test_preprocessing.py::TestPreprocessingFlow::test_preprocessing 
-------------------------------- live log call --------------------------------
2021-12-03 09:38:20 [    INFO] Establishing connection... (preprocess_handler.py:72)
2021-12-03 09:38:20 [    INFO] Creating session in eu-west-1 (connection.py:75)
2021-12-03 09:38:20 [    INFO] Found credentials in shared credentials file: ~/.aws/credentials (credentials.py:1225)
```

Hope this helps!

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
