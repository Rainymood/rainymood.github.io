---
title: "Refactoring code so that it becomes easier to test"
date: 2022-05-27
tags:
- blog
- jekyll
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2022-05-27-refactoring-using-tdd/thumbnail.png"
---

I refactored a piece of code but I'm not sure if I made it better.

**This is the code before.** 
It grabs an object from s3, unpacks it, and passes it through a csv reader
turning it into a list of dicts.


```python
def read_csv_data(self, bucket_name, key):
    s3_object = self._s3_resource.object(bucket_name, key)
    data = s3_object.get()['body'].read().decode('utf-8').splitlines()
    return [*csv.dictreader(data)]
```

**This is the code after.**
The main thing I did was pull out the decoding in a separate function and added
some type hints (because type hints are love).

```python
from typing import List, Dict

def decode_s3_object(self, s3_object) -> List[str]: 
    return s3_object.get()['body'].read().decode('utf-8').splitlines()

def read_csv_data(self, bucket_name: str, key: str) -> List[Dict[str, str]]:
    s3_object = self._s3_resource.object(bucket_name, key)
    data = self.decode_s3_object(s3_object)
    return [*csv.dictreader(data)]
```

**Had trouble mocking.** 
The reason I pulled out this function was because I had trouble mocking the
`data` variable. At some point I got so annoyed at myself I just said "Screw it
I'll put it in a separate function."

**Short functions are easier to test.**
With short functions you end up writing more tests because the tests are easier
to write. And the tests are easier to write because your functions are short. In
that sense, short functions and tests form a positive feedback loop together. I
found it much easier to write two tests for the second version than a single
test for the first version because in the second case I could mock the output
of `decode_s3_object`.

Anyway, what do you think? Did the code improve by pulling out this function?

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