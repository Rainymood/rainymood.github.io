---
title: "Use assertions to check tensor sizes"
date: 2023-02-10
tags:
- programming
- pytorch
- tensorflow
- python
- machine learning
- lessons learned
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2023-02-10-use-assertions-to-check-tensor-sizes/thumbnail.png"
---

This is another post in the series [lessons learned building machine learning systems]({% post_url 2022-12-21-lessons-learned-from-building-machine-learning-systems %}).

What I found very useful from personal experience is to **use assertions to check the sizes of your tensors.**

Pepper your machine learning code with assertions that validate the sizes of your tensors like this:

```python
assert dot_product.size() == input_exercise_bias.size()  # (batch_size,)
```

This may sound redundant and excessive, but you'll be happy when it triggers when you change something somewhere else:

```python
dot_product = torch.einsum("ij,ij->i", hidden_state_batch, input_exercise_embedding)
    
>       assert dot_product.size() == input_exercise_bias.size()  # (batch_size,)
E       AssertionError
```

Which triggered because a tensor changed from `torch.size([42, 1])` to `torch.size([42])`

```python
input_exercise_bias.size()
Out[4]: torch.Size([42, 1])
dot_product.size()
Out[5]: torch.Size([42])
```

You will find resistance to this idea because it does not produce clean code. But you will be very happy once one of them triggers. 

It is easy to think that we do not make mistakes. But the problem is that we do.

These assertions are just quick and hacky in place tests, so they are not a replacement for tests but more of a supplement.

Assertions on shapes of your tensors are a low effort, high reward hack. So use them wisely.

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
    