---
title: "What if your code and tests are in the same file?"
date: 2024-05-02
tags:
# Blog or how-to
- blog
# Work or personal?
- work
# Big themes that I write about
- engineering
- testing
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2024-05-02-what-if-your-code-and-tests-are-in-the-same-file/thumbnail.png"
---
<!-- ctrl + alt + v -->

I talked about co-locating code and tests before in my blog called [Should you colocate your tests? A proof-of-concept]({% post_url 2024-01-03-should-you-colocate-your-tests-a-proof-of-concept %}).

What if we take this concept even a step further and put the code and tests **in the same file**?!

Something like this:

```python
import pytest

test_add_table = [
    (0,0,0),
    (1,1,2),
    (3,4,7),
    pytest.param("0", 1, 1, marks=pytest.mark.xfail)
]
@pytest.mark.parametrize("a,b,res", test_add_table)
def test_add(a,b,res):
    assert add(a,b) == res

def add(a: int, b:int) -> int:
    return a + b

if __name__ == "__main__":
    print(add(10, 10))
```

I think this is a crazy idea and honestly I think it would get very messy, but
I'm all out for trying such a crazy idea once just to better understand why it
wouldn't work. 

Find the full code on Github [here](https://github.com/Rainymood/pytest-same-file).

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
    