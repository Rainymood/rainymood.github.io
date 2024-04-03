---
title: "Never Integrate Directly"
date: 2024-04-03
tags:
# Blog or how-to
- blog
- tutorial

# Work or personal?
- work
- personal

# Big themes that I write about
- engineering
- management
- leadership
- systems
- productivity

# Programming languages/Cloud
- rust
- golang
- python
- sql
- javascript
- aws
- testing
- documentation

# Smaller themes
- writing
- product
- design
- tools
- learning

- advent of code
- aws 
- docker
- machine learning
- programming
- pytorch
- tensorflow
- code
- show-your-work
- tip
- athena

- meta programming
- architecture

- flashcards
- projects
- startups

- cosmicpython
- inversion of control
- domain driven design

- story
- lessons learned
- video games

categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2024-04-03-never-integrate-directly/thumbnail.png"
---
<!-- ctrl + alt + v -->

<!-- 1. interesting hook -->

Here’s a golden tip for you when developing software: **never integrate directly**.

All issues, big and small, in my current project stem from the fact that we integrated directly instead of indirectly.

[Arvid Kahl writes](https://thebootstrappedfounder.com/zero-to-sold/guide/#:~:text=Here%20is%20a,need%20to%20change.):

> Here is a general rule for integrating a third-party-service: never integrate the service directly. The service should always be integrated through an abstraction. 
> 
> For example, let’s say you are integrating MailChimp into your backend server. Instead of using the MailChimp URLs directly in your code, build a class or module responsible for interacting with Email List services that handle all the specific calls internally. That way, your Email List module can later easily integrate a different service like Email Octopus, raw AWS SNS, or ConvertKit if you ever feel the need to change.

For a bit of context on the project, my team is working on putting some models that our data scientists made into production.

They expose their code as a package and we write some infrastructure as code around it to serve it.

Now, an astute observer can already see what is wrong here, the dependency flow is wrong. It is the other way around. We are the platform team yet we depend on rapidly changing code. 

It should be the other way around, we should write the platform and the data scientists should hold the implementation details of our platform. 

But alas, we did not have the time to write the platform first, so here we are.

Let’s look at some concrete examples where we violated this maxim of never integrating directly

### Example 1: Directly integrating a rapidly changing package

The first thing we did wrong was that we directly integrated with their package. Like so

```python
# pip install external_datascience_package

from external_datascience_package.entrypoints import predict

data = predict.main(prediction_args)
```

Oops! 

This does not *seem* wrong, but what *is* wrong with this direct integration?

On the surface it looks like this is fine, right? 

What happend in reality is that their code kept changing, and we kept updating the contracts, but sometimes human mistakes slipped in and documentation was not updated, leading to quite some frustration.

For example, they had a very useful `--test-mode` flag that worked great for them, but when we started using it with our settings we ran into inconsistent results, leading to very brittle code.

Mocking their package as a function was slightly more difficult because now we had to mock a function from a package.

All of this could have been avoided if we had just abstracted away from it behind an interface, allowing us to return mocked values for our own local interface implementation.

### Example 2: Directly integrating with s3

Another mistake we made was integrating s3 directly.

I tried to avoid this one like the plague, but I ended up succumbing to some time pressure because of a technical issue we were not able to solve in time. 

```
s3_client.put_object(
    Bucket=bucket,
    Key=str(s3_filepath),
    Body=json.dumps(res, default=str),
)
```

Oops I did it again. 

We integrated directly. This time with s3.

Our initial setup that I strongly preferred wrote to disk locally and used Sagemaker pipelines to figure out where the files should be uploaded to s3.

But it turns out that it is impossible to **remove the encryption** from Sagemaker written artefacts, this led to encryption errors from teams that were dependent on the output we generated. 

This forced us to get rid of this feature we used from Sagemaker and manually start uploading the files to s3, strongly coupling our application to s3.

Honestly, this one is not so bad.  Mocking out s3 is fairly easy. But from an architectural point of view it is better to hide this also behind an interface so that you can swap out the s3 for a mocked s3 in the tests and be done with it.

### Conclusion

When integrating a third-party service or external service, never integrate directly. 

Hide the implementation behind an interface that allows you to mock the response that you would expect.

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
    