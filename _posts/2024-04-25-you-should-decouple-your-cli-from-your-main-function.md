---
title: "You should decouple your cli from your main function"
date: 2024-04-25
tags:
# Blog or how-to
- tutorial

# Work or personal?
- work

# Big themes that I write about
- engineering
- software architecture
- python

categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2024-04-25-you-should-decouple-your-cli-from-your-main-function/thumbnail.png"
---
<!-- ctrl + alt + v -->

<!-- Automotive tools floating 3d render,oil falling from the sky,nuts and bolts, industrial design unreal engine 5 -->

Many of my colleagues are working on writing better code, so I'm sharing a little tip that I find very useful.

Your `main()` function should be independent of the `argparser`. 

You should be able to drive your application from *both* the cli/terminal (using the `CliAdapter`) *and* for example your tests (using the `TestAdapter`). 

I have written about this before here in [Your argparse is not the interface of your application]({% post_url 2023-02-18-your-argparse-is-not-the-interface-of-your-application %}).

Let me illustrate:

```python
"""
Example script to show how to decouple your application from the CLI.

Your CLI shouldn't be the interface to your application, it should just be one
way of driving the application.

Notice how main() is decoupled from the CLI. It knows nothing about how to parse
arguments.
"""
import argparse
from abc import abstractmethod, ABC
from pydantic import BaseModel

class InputModel(BaseModel):
    value: int

class InputInterface(ABC):
    @abstractmethod
    def parse(self, args) -> InputModel:
        raise NotImplementedError

class CliAdapter(InputInterface):
    def parse(self, args) -> InputModel:
        parser = argparse.ArgumentParser(description='Process an integer.')
        parser.add_argument('integer', type=int, help='An integer value')
        args = parser.parse_args(args)
        return InputModel(value=args.integer)

class TestAdapter(InputInterface):
    def parse(self, args) -> InputModel:
        return InputModel(value=10)

def main(input: InputModel):
    print(input.value)

if __name__ == "__main__":
    # In your main entrypoint
    cli = CliAdapter()
    input = cli.parse(["10"])
    main(input)

    # In a pytest fixture and test code
    test = TestAdapter()
    input = test.parse(None)
    main(input)
```

Your `main()` should not care whether it gets the arguments from the cli or from
any other adapter. If it gets a correct `InputModel` it should just run.

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
    