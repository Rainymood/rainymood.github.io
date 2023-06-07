---
title: "My experience with DDD (part 2)"
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
* [test]({% post_url 2023-06-02-my-experience-with-domain-driven-design-part-1.md %})

## Test object creation also goes into fixtures

In my previous post I told you that we heavily rely on [pytest fixtures]() to set up everything, but we take this even a step further. We even make our test objects in fixtures so that we can easily reuse them.

First I wanted to create my `ContextDataTransformer` and test it like so

```python
def test_context_data_transformer_has_right_schema(non_sequential_raw_dataset, non_sequential_raw_mappers):
    transformer = ContextDataTransformer(
        ...
    )

    assert transformer.get_schema() == expected_schema
```

But looking at the other tests I noticed we had a fixture that contained some data. In this fixture some objects were also created. So instead of creating the test object in the test, we create it in the fixture:

```python
# tests/fixtures/data_transformation_fixture.py
@pytest.fixture
def snappet_pupil_to_dense_sequence_transformer(non_sequential_raw_mappers):
    return DictionaryTransformer(
            output_fields=[DENSE_PUPIL_ID_SEQUENCE],
        ),
        dictionary=non_sequential_raw_mappers["snappet_pupil_id_to_dense"],
        default_value=-1,
    )
``` 

Before

```python
def test_context_data_transformer_has_right_schema(non_sequential_raw_dataset, non_sequential_raw_mappers):
    transformer = ContextDataTransformer(
        snappet_originalexercise_id_mapper=non_sequential_raw_mappers["snappet_originalexercise_id_to_dense"],
        snappet_answer_type_mapper=non_sequential_raw_mappers["snappet_answer_type_to_dense"],
        default_value=0,
    )

    expected_schema = InputOutputSchema(
        input_schema=Schema(fields=[SNAPPET_ORIGINAL_EXERCISE_ID, SNAPPET_ANSWER_TYPE]),
        output_schema=Schema(fields=[DENSE_CONTEXT_ID]),
    )

    assert transformer.get_schema() == expected_schema
```

After

```python
def test_context_data_transformer_has_right_schema(snappet_context_data_transformer):
    transformer = snappet_context_data_transformer

    expected_schema = InputOutputSchema(
        input_schema=Schema(fields=[SNAPPET_ORIGINAL_EXERCISE_ID, SNAPPET_ANSWER_TYPE]),
        output_schema=Schema(fields=[DENSE_CONTEXT_ID]),
    )

    assert transformer.get_schema() == expected_schema
```

What this means is that we also create the objects we want to test in our fixtures. 

The test code is much cleaner now.

The main benefit of doing this, I think, is that you only really have one place where all the objects are now which are the fixtures. 

## Tests become extremely lightweight

I've said this before and I will say it again: having things defined in terms of your domain model makes your tests really lightweight. 

All your domain models and where they are made are centralised in the fixtures. You have also thought about what data you need and hence you make the smallest possible version of that data, which makes everything light.

All of these things seem small when you look at them in isolation: thinking about your test data, putting them in fixtures, writing tests in terms of domain models. But when you add them up they amount to a test suite that is a joy to run. The testing experience, honestly, is joyful instead of soul-sucking. 

I'm not afraid of changing things anymore because the tests are nimble and fast. If I change something I know that the tests will run in 50ms or so, so no fear in changing things. I can change something, get feedback, adjust, and adapt. It's great. 

## Constructing a mental model of the problem

A big part of domain-driven design is crafting a domain language that is understood by everyone (shared vocabulary) but at the same time that helps you solve the problem.

A big part of problem solving, using code then, is trying to create a mental model of the problem in your head and being able to swiftly traverse around that mental model. Of course, some problems are complex, and that makes the mental models quite large and bit so it might take a while to get accustomed to the new mental model, this is nothing new.

Similarly, working with this new repository that uses a domain model I needed to get my head around the domain model first. After a couple of days of struggling I feel like I'm getting the overall picture, the "gestalt" of things. 

## Schema validation is nice

The first time I wrote this I thought the data validation was excessive and trivial:

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

And then the first time I tried to run a test, it already triggered and saved me a bug. Humans are flawed sometimes. Hehe. 

## Our domain model makes indexing batches a breeze

Another really neat thing is that I can index our data with the `Field.name` instead of an index. 

Previously, `batch_data` would just be a dataframe or tensor and we would have to slice it like this: 

```python
dense_original_exercise_ids = batch_data[:1]
```

Now with our domain model where `data` is a `Data` object that is a list of `Fields` we can instead slice with the `Field.name`: 

```python
dense_original_exercise_ids = data[DENSE_ORIGINAL_EXERCISE_ID]
```

This is really neat.

## Tests run in the order of ms

![](/../assets/2023-06-06-my-experience-with-ddd-part-2/2023-06-06-13-48-08.png)

Which really is a great feeling.

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
    