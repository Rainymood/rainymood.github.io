---
title: "How to get bucket name and key for s3 urls in python"
date: 2022-12-12
tags:
- blog
- python
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2022-12-12-how-to-get-bucket-name-and-path-for-s3-urls-in-python/thumbnail.png"
---

If you work a lot with s3 urls like these

```bash
url = "s3://some-bucket-name/dataset-name/some-folder"
```

Then this can come in handy. I found this on [StackOverflow](https://stackoverflow.com/a/42641363):

```python
from urllib.parse import urlparse 
class S3Url(object): 
    # From: https://stackoverflow.com/questions/42641315/s3-urls-get-bucket-name-and-path
    def __init__(self, url): 
        self._parsed = urlparse(url, allow_fragments=False) 

    @property 
    def bucket(self): 
        return self._parsed.netloc 

    @property 
    def key(self): 
        if self._parsed.query: 
            return self._parsed.path.lstrip("/") + "?" + self._parsed.query 
        else: 
            return self._parsed.path.lstrip("/") 

    @property 
    def url(self): 
        return self._parsed.geturl()
```

Works like a charm!

```python
s = S3Url("s3://bucket/hello/world")  
print(s.bucket)  # 'bucket'  
print(s.key)  # 'hello/world' 

s = S3Url("s3://bucket/hello/world?qwe1=3#ddd")  
print(s.bucket)  # 'bucket'  
print(s.key) # 'hello/world?qwe1=3#ddd'
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
  <label for="mce-EMAIL">I blog about how to grow as a machine learning engineer! Liked this article and want to hear more? Join 40+ others and subscribe!</label>
  <input type="email" value="" name="EMAIL" class="email" id="mce-EMAIL" placeholder="email address" required>
    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
    <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_92fe86c389878585bc87837e8_50543deff9" tabindex="-1" value=""></div>
    <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button"></div>
    </div>
</form>
</div>
<!--End mc_embed_signup-->

