---
title: "Tip: Use pytest fixtures instead of test data"
date: 2023-06-01
tags:
- programming
- code
- tip
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2023-06-01-tip-use-pytest-fixtures-instead-of-test-data/thumbnail.png"
---
<!-- ctrl + alt + v -->

Recently I've been using a lot of [pytest fixtures](https://docs.pytest.org/en/6.2.x/fixture.html) instead of a `tests/data` folder and my life has been much better ever since!

## What are fixtures?

From the [pytest docs](https://docs.pytest.org/en/6.2.x/fixture.html)

> Software test fixtures initialize test functions. They provide a fixed baseline so that tests execute reliably and produce consistent, repeatable, results. These are accessed by test functions through arguments; for each fixture used by a test function there is typically a parameter (named after the fixture) in the test function’s definition.

For example

```python
import pytest
import pandas as pd

@pytest.fixture
def my_df():
    return pd.DataFrame({"foo": [1,2,3]})

def test_df(my_df): # <= my_df now refers to the fixture 
    assert do_something(my_df) 
```

This is what happens when you don't have to think about your test data...

## ❌Don't: Use test data 

Without fixtures you don't really have to think about your test data, so without proper guardrails it becomes a mindless append-only fiesta. Look at this (very real) test data folder over 1gb! 

![](/../assets/2023-06-01-tip-use-pytest-fixtures-instead-of-test-data/2023-06-01-11-45-32.png)

And this is your repository on fixtures:

## ✅ Do: Use pytest fixtures

With fixtures you keep test data in code, and that means that you have to be more intentional about it. You have to think about what is the smallest piece of data that you need for your test to pass. By virtue of thinking this through you create lightweight test structures that make everything else that it touches also light.

```python
@pytest.fixture
def raw_dataset_df():
    data = {
        "pupilid": [1, 2],
        "exerciseid": [3, 4],
        "correct": [1, 0],
    }
    yield pd.DataFrame(data=data)
```

# Conclusion

The simple act of using [pytest fixtures](https://docs.pytest.org/en/6.2.x/fixture.html) over a folder with test data has made our repositories significantly lighter (in terms of raw files) and our code significantly better. I highly suggest you try it out!

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
<label for="mce-EMAIL">I blog about how to grow as a machine learning engineer! Liked this article and want to hear more? Join 40+ others and subscribe!</label>
<input type="email" value="" name="EMAIL" class="email" id="mce-EMAIL" placeholder="email address" required>
    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
    <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_92fe86c389878585bc87837e8_50543deff9" tabindex="-1" value=""></div>
    <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button"></div>
    </div>
</form>
</div>
<!--End mc_embed_signup-->
    