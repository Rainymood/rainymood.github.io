---
title: "How to test for specific error message in pytest.raises()"
date: 2022-06-17
tags:
- blog
- jekyll
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2022-06-17-how-to-test-for-specific-error-message-in-pytestraises/thumbnail.png"
---

[Pytest](https://docs.pytest.org/en/7.1.x/) makes it very easy to test the *content* of the error message you get from a raised exception using the `match` argument. See the documentation [here](https://docs.pytest.org/en/latest/reference/reference.html#pytest.raises). 

I query a lot of SQL from Jupyter notebooks

```python
ath.query_database("SELECT foo, bar FROM t limit 10")
```

And if something goes wrong we raise a `ConnectionError`

```python
---> 83     raise ConnectionError("query status: {0:s}".format(result["QueryExecution"]["Status"]["State"]))

ConnectionError: query status: FAILED
```

But this error is not so helpful because it doesn't tell me *why* the query failed. 

So I changed it

```python
---> 83     raise ConnectionError(f"Query {status}: {error_msg}")

ConnectionError: Query FAILED: line 1:22: Table data_catalog.data_warehouse.t does not exist
```

But how do I write a test for this? 

Turns out that pytest makes it easy to test for a *specific* error message using the `match` keyword. 

This is the test I wrote

```python
def test_query_better_error_message(self):
    # Given
    query_string = "SELECT foo, bar FROM t limit 10"
    err_msg = "Query FAILED: line 1:22: Table data_catalog.data_warehouse.t does not exist"

    # When + Then
    with pytest.raises(Exception, match=err_msg) as e:
        ath.query_database(query_string)
``` 

So you can run `pytest.raises()` and then `match=..` the string you want your error to be. Super useful for this kind of stuff. It can also be a regex if you need more flexibility.

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
