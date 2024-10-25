---
title: "How to efficiently compress a list of integers with a maximum value in Python"
date: 2024-10-26
tags:
# Blog or how-to
- blog
# Work or personal?
- work
# Start here themes
- software
# Big themes that I write about
- engineering
- python
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2024-10-26-how-to-compress-a-list-of-integers-in-python/thumbnail.png"
---
<!-- ctrl + alt + v -->

I want to share a quick piece of code that I've been using and reusing a lot. Right now in the current projects that I'm working on I have to store a lot of data and store it efficiently. We are talking millions of states that need to be stored in small packets of less than 4kb. Here, compression and efficient storage become important. I find myself reusing this trick very often so I want to share it with you guys in the hope that it is useful to you too.

Imagine you have a list of integers `lst = [1,2,3.., 100, 2, 3, 100]` in Python that you need to compress, but you also know that this list has a maximum value (100 in this case).

What you can then do, if you want to compress and store this array, is the following: pack it into bytes, compress it with `zlib`, and then `base64` encode it. 


```python
class CappedIntBlob(List[int]):
    """Capped integer Base64 Large Object aka CappedIntBlob.
    
    Represents a list of 2-byte unsigned short integers, capped at xxxx.

    When converted to str, will convert all integers into 2-byte values and then base64 encode them after compressing with zlib.

    The constructor accepts either a base64 string or an iterable
    of integers.
    """

    def __init__(self, contents: Union[str, Iterable[int]], max_val: int = 10):
        """Constructor
        @param contents: the contents, either a list of ints or a base64 string with 2-byte unsigned short integer representation.
        """
        self.max = max_val
        lst: Iterable[int]
        if isinstance(contents, str):
            # If input is a string, decode and decompress it
            bs: bytes = zlib.decompress(base64.b64decode(contents))
            # < = little endian, H = unsigned short with 2-byte size integers
            lst = struct.unpack("<" + "H" * int(len(bs) / 2), bs)
        elif isinstance(contents, Iterable):
            lst = [min(int(x), self.max) for x in contents]
        else:
            raise ValueError("Expecting a string or an iterable for contents")

        super().__init__(lst)

    def __str__(self):
        """Convert to string
        @return: base64 string encoding for list of ints in 2 byte unsigned short integer representation.
        """
        return base64.b64encode(zlib.compress(struct.pack("<" + "H" * len(self), *self))).decode("utf-8")
```

And this is how you use it

```python
>>> CappedIntBlob([1,2,3])
[1, 2, 3]

>>> str(CappedIntBlob([1,2,3]))
"eJxjZGBiYGYAAAAaAAc="

>>> CappedIntBlob("eJxjZGBiYGYAAAAaAAc=")
[1, 2, 3]

assert str(CappedIntBlob([5, 10, 20])) == str(CappedIntBlob([5, 100, 200])) # true
```


https://app.bannerbear.com/projects/POobgvMNDkxzxAYW70/templates/3g8zka5Y2OlaDEJXBY

https://www.photopea.com/



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
    