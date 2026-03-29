---
title: "I like this abstraction"
date: 2026-03-29
tags:
- work
- software
- software architecture
- aws
- machine learning
- python
- practical-advice
- code
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2026-03-29-i-like-this-abstraction/thumbnail.png"
---
<!-- ctrl + alt + v -->
<!-- cmd + alt + v -->

At work, we host a lot of inference endpoints and for that we use [Sagemaker](https://aws.amazon.com/sagemaker/). Sagemaker uses this abstraction, and I've grown quite fond of it:

- `default_model_fn(model_dir, context=None)`: This loads in the model and acts as a `setup()` function. This returns the model and other related services that your endpoint needs.
- `default_input_fn(input_data, content_type, context=None)`: This is basically an input adapter. Take the raw unsanitzed input in string or bytes and parse it. This returns validated input.
- `default_predict_fn(data, model, context=None, )`: This is your bread and butter, take the model (and other related services) and make a prediction by passing it to `model.forward()`. This returns a prediction.
- `default_output_fn(prediction, accept, context=None)`: This is basically an output adapter. Take the prediction the model made, serialize it to whatever output type you need your endpoint to spit out. This returns serialized output.

<!-- Holy shit! I can just ask the LLM to do the tags for me! "pick out the right tags and edit the front yaml" --> 
