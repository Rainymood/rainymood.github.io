---
title: "My experience with Domain-Driven Design part 2: testing"
date: 2023-06-06
tags:
- programming
- python
- code
- domain driven design
- work
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2023-06-06-my-experience-with-ddd-part-2/thumbnail.png"
---



Previous editions:
* [My experience with Domain Driven Design part 1]({% post_url 2023-06-02-my-experience-with-domain-driven-design-part-1 %})

## Use fixtures for test object creation

Another new thing that I noticed is that we setup our objects that we want to test *inside pytest fixtures*. 

Before I would do something like this (you do not need to know what a `ContextDataTransformer` is)

```python
def test_context_data_transformer_has_right_schema():
    transformer = ContextDataTransformer()

    assert transformer.get_schema() == expected_schema
```

But we can *also* put the object creation inside the fixture, making the test a lot cleaner

```python
# tests/fixtures/data_transformation_fixture.py
@pytest.fixture
def context_data_transformer():
    return ContextDataTransformer()
``` 

Which means that now in our test we can rely on the fixture instead

```python
def test_context_data_transformer_has_right_schema(context_data_transformer):
    assert transformer.get_schema() == expected_schema
```

Essentially we are just moving things around from the test file to the fixture file, but I notice that my tests feel a lot cleaner because they only test the behavior of the object or function under test.

## Tests become extremely lightweight

I've said this before and I will say it again: using a domain model makes your tests really lightweight.

Because you have thought deeply about your domain model you know the minimum amount of data you need to construct them, which results into small fixtures, which again results in quick tests. 

## Constructing a mental model of the problem

I think that domain driven design and problem solving with it is like learning a new language. It takes some time to get up to speed with the vocabulary and grammar. 

A big part of problem solving is trying to create a mental model of the problem that helps to solve said problem. Then you should load this mental model into your head and be able to swiftly traverse up and down the necessary ladders of abstraction. Some problems are quite big and thorny which makes their mental models also big and thorny, so it might take a while to get accustomed to this new mental model. 

What I want to say is that it's not weird to have to study the domain model for quite some time, say 2 days, to become well-versed in it. You need to understand all the individual pieces before you can really wrap your head around it and grok the overallness of the project, the gestalt. 


## Schema validation is nice

When I wrote this I thought it was very extra, "Who needs data validation?" I
thought to myself. I thought I was smart and good at writing code:

```python
def transform(self, data: Data):
    input_schema = set(self.schema.input_schema.fields)
    data_schema = set(data)
    is_schema_valid = input_schema.issubset(data_schema)
    if not is_schema_valid:
        raise ValueError(
            f"The input_data data does not contain the fields this transformer supports:"
            f"{self.schema.input_schema.fields[0]}."
        )
```

The first time I wrote a test for the `transform` function the invalid schema
immediately triggered because of an error I made. Oopsy!


## Our domain model makes data indexing a breeze

Our domain model works like this, we have a `DataLoader` that provides batches of `Data` which are dicts indexed with keys of `Fields`. 

Previously, `batch_data` would just be a dataframe or tensor and we would have to slice it like this: 

```python
dense_original_exercise_ids = batch_data[:1]
```

Now with our domain model where `data` is a `Data` object that is a list of `Fields` we can instead slice with the `Field.name`: 

```python
dense_original_exercise_ids = data[DENSE_ORIGINAL_EXERCISE_ID]
```

This is really neat.

## Wrapping up 

In isolation, all these things are small improvements: small data, pytest fixtures, fast tests. But small things add up. When you add them all up your testing experience suddenly becomes a joy instead of a drag. Tests run in the order of 50ms which makes it almost (gasp) fun to run your tests because they are so damn quick. I'm not afraid of changing things because I know I can run the tests, get quick feedback, and adjust and adapt. The testing experience becomes joyful instead of a soul-sucking tedium. 

**Remember** Domain-driven design makes the testing experience much more joyful
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
    