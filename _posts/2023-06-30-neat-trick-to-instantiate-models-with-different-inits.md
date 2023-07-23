---
title: "Neat trick to instantiate models with different inits"
date: 2023-06-30
tags:
- python
- code
- tip
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2023-06-30-neat-trick-to-instantiate-models-with-different-inits/thumbnail.png"
---

In this blog post I want to share with you a trick that I find myself using quite often when trying to instantiate different machine learning models with different parameters in the same machine learning pipeline.

I use this trick to keep my training code generic and model-agnostic while writing machine learning code.

We start from a simple model interface that implements a forward pass

```python
from abc import ABC, abstractmethod

class ModelInterface(ABC):
    @abstractmethod
    def forward(self):
        raise NotImplementedError
```

Our first model, model A, is instantiated with a variable specifying the latent dimensions:

```python
class ModelA(ModelInterface):
    def __init__(self, latent_dim):
        self.latent_dim = latent_dim

    def forward(self):
        print(f"fwd pass with latent_dim={self.latent_dim}")
```

Our second model, model B, is instantiated with a different variable specifying the number of embeddings: 

```python
class ModelB(ModelInterface):
    def __init__(self, num_embeddings):
        self.num_embeddings = num_embeddings

    def forward(self):
        print(f"fwd pass with num_embeddings={self.num_embeddings}")
```

How do we now write generic code that can handle both these models?

Let me show you.

First, and this is extra, we create an identifier enum for each model: 

```python
from enum import Enum

class ModelIdentifier(Enum):
    ModelA = "ModelA"
    ModelB = "ModelB"
```

Then, we create the model map, mapping the identifier to the model

```python
model_name_to_model = {
    ModelIdentifier.ModelA: ModelA,
    ModelIdentifier.ModelB: ModelB,
}
```

Now, using dictionary unpacking we can use this model map in combination with the model identifier to choose the right model and instantiate it!

Consider model A for example:

```python
config_a = {
    "latent_dim": 10,
}
model = model_name_to_model[ModelIdentifier.ModelA](**config_a)
model.forward() # Results in: fwd pass with latent_dim=1
```

And consider model B now with a different config

```python
config_b = {
    "num_embeddings": 1,
}
model = model_name_to_model[ModelIdentifier.ModelB](**config_b)
model.forward() # Results in: fwd pass with num_embeddings=1
```

Of course, this wouldn't work if we did not adhere to the interface, but if you stay true to the interface, then this can come in handy. That's it! Until next time!

**Remember** You can use dictionary unpacking (`**my_dict`) in combination with an interface to instantiate models with different parameters!
{: .notice--success}

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
    

