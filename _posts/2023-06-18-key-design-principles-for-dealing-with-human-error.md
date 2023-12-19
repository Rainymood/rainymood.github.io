---
title: "Key design principles for dealing with (human) error"
date: 2023-06-18
tags:
- systems
- work
- design
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2023-06-18-key-design-principles-for-dealing-with-human-error/2023-06-18-17-52-52.png"
---
<!-- ctrl + alt + v -->

<img src="/assets/2023-06-18-key-design-principles-for-dealing-with-human-error/2023-06-18-18-30-42.png" style="max-height: 200px">{: .align-left} 
When I picked up this book I thought it was going to be a book about product design. That was true, but this book is also much more. Next to being extremely entertaining and informative, it provides a unified framework for thinking about usability in products. 

## Two gulfs

Given a user and product we can always describe two fundamental user-product discrepancies: 

* **Gulf of execution**: The gap in what the user wants to do (goals) and how easy it is for the user to figure out how to do it (feedfoward)
* **Gulf of evaluation**: The gap in what the user did and how easy it is for the user to figure out what happened and to course correct (feedback)

A simplified version of the model is illustrated here:

![](/../assets/2023-06-18-key-design-principles-for-dealing-with-human-error/2023-06-18-17-59-33.png){: .align-center}

## Key design principles

Because we, as humans, are fallible, human error is inevitable. Thus, the best designs take this into account. These are the key design principles from the book for dealing with (human) error, I quote (emphasis mine): 

* "**Put the knowledge required to operate the technology in the world**. Don’t require that all the knowledge must be in the head. Allow for efficient operation when people have learned all the requirements, when they are experts who can perform without the knowledge in the world, but make it possible for non-experts to use the knowledge in the world. This will also help experts who need to perform a rare, infrequently performed operation or return to the technology after a prolonged absence."
* "Use the power of natural and artificial constraints: physical, logical, semantic, and cultural. Exploit the power of forcing functions and natural mappings."
* "Bridge the two gulfs, the Gulf of Execution and the Gulf of Evaluation. **Make things visible, both for execution and evaluation.** On the execution side, provide feedforward information: make the options readily available. On the evaluation side, provide feedback: make the results of each action apparent. Make it possible to determine the system’s status readily, easily, accurately, and in a form consistent with the person’s goals, plans, and expectations."

## Wrapping up

For me, this summarizes to the following two statements: 

1. Keep in mind the two gulfs (execution and evaluation)
2. Make everything visible: knowledge on how to operate the system, but also feedback and feedforward

**Remember** The best design takes human error into account.
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
    