---
title: "Rebind shift + cmd + m to %>% (pipe symbol)" 
date: 2020-08-26
categories:
  - blog
tags:
  - blog
  - karabiner-elements
header:
  teaser: "/assets/2020-08-26-rstats-binding/teaser-rstats-1280x700.png"
---

I recently made a [video](https://www.youtube.com/watch?v=iiSIaMD4vqY) about
how to make custom complex modifications in
[Karabiner-elements](https://github.com/pqrs-org/Karabiner-Elements). Someone
saw this video and reached out to me for some help.

![](/assets/2020-08-26-rstats-binding/request.png)

It took me a few days, but I found a solution to his problem! 

# What didn't work

My first try looked something like this. 

```json
...
"from": {
    "key_code": "m",
        "modifiers": {
            "mandatory": ["command", "shift"]
        }
},
"to": [
    {
        "key_code": "5",
        "modifiers": {
            "mandatory": ["left_shift"]
        }
    },
    {
        "key_code": "period",
        "modifiers": {
            "mandatory": ["left_shift"]
        }
    },
    {
        "key_code": "5",
        "modifiers": {
            "mandatory": ["left_shift"]
        }
    }
],
...
```

*"This should definitely work."* I thought to myself. But it didn't.

Thankfully, I was smart enough to check out the logs and found this.

![](/assets/2020-08-26-rstats-binding/log.png)

# What did work

There is a simple reason why my previous solution didn't work. 

Notice that for multiple arguments, the value of the `modifiers` key must be
a `list`.

The error message tells us that for a single argument the value of the
`modifiers` key must be a `string`!

We now have a simple fix by changing `"mandatory": ["left_shift"]` into
`"mandatory": "left_shift"` and voila! We are done.

```json
{
    "title": "Rstats pipe symbol (by @janmeppe)",
    "rules": [
        {
            "description": "Remaps shift + cmd + m to %>%",
            "manipulators": [
                {
                    "from": {
                        "key_code": "m",
                            "modifiers": {
                                "mandatory": ["command", "shift"]
                            }
                    },
                    "to": [
                        {
                            "key_code": "5",
                            "modifiers": {
                                "mandatory": "left_shift"
                            }
                        },
                        {
                            "key_code": "period",
                            "modifiers": {
                                "mandatory": "left_shift"
                            }
                        },
                        {
                            "key_code": "5",
                            "modifiers": {
                                "mandatory": "left_shift"
                            }
                        }
                    ],
                    "type": "basic"
                }
            ]
        }
    ]
}
```

# Conclusion

In this blog post I show you how to create a custom complex modification in
Karabiner-elements to remap `shift + cmd + m` to `%>%` which is the pipe
symbol in R. Hopefully some Rstats people find this useful! 

Also, remember to check your error logs!

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
  <label for="mce-EMAIL">Liked this article and want to hear more? Join 53 others and subscribe!</label>
  <input type="email" value="" name="EMAIL" class="email" id="mce-EMAIL" placeholder="email address" required>
    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
    <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_92fe86c389878585bc87837e8_50543deff9" tabindex="-1" value=""></div>
    <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button"></div>
    </div>
</form>
</div>
<!--End mc_embed_signup-->