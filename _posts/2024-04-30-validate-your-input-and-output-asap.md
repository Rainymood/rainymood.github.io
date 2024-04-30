---
title: "Validate your input and output ASAP"
date: 2024-04-30
tags:
# Blog or how-to
- blog
# Work or personal?
- work
# Big themes that I write about
- engineering
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2024-04-30-validate-your-input-and-output-asap/thumbnail.png"
---
<!-- ctrl + alt + v -->

If there is one thing that I've learned recently is that you really want to validate your inputs and outputs early.

Assuming you are some machine learning or software engineer and you are building a service that takes some data from somewhere, does something with it, and then puts that transformed data somewhere else.

The **very first thing** you should do is to validate your inputs and validate your outputs.

Get a test like this up and running ASAP. It will save you a lot of headache down the line.

```python
def test_integration():
    # ... main routine ...
    f = download_as_json(bucket, key)
    try:
        data_model.model_validate(f) # datamodel = pydantic.BaseModel
    except pydantic_core._pydantic_core.ValidationError as ve:
        logger.info(f"Failed validating json: {json.dumps(f, indent=2)} ")
        assert 0
    logger.info(f"Successfully validated json: {json.dumps(f, indent=2)}")
    assert 1
``` 

When you have data coming in your want to be **really sure** that what you take in is really what you think you take in. 

For example, we thought we would get a `pd.DataFrame` with a list of integers, but it turns out that if these are nullable then pandas turns this into a list of floats!

When you have data coming out you want to be **really sure** that what you spit out is actually what you want to spit out.

For example, we thought we were writing `"1"` stringified ints, but because of the above mentioned it turned into `"1.0"`. 

Moral of the story is this: get some input and output checking up asap. [Pydantic](https://docs.pydantic.dev/latest/) is great for this.



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
    