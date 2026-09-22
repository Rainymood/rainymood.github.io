---
title: "Why things take longer than we think"
date: 2026-06-08
tags:
- work
- productivity
- engineering
- software
- lean
- management
- lessons learned
- practical-advice
- story

categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2026-06-08-why-things-take-longer-than-we-think/thumbnail.png"
---
<!-- ctrl + alt + v -->
<!-- cmd + alt + v -->

Why do things always take longer than we think? 

How can we always tend to underestimate the time it takes to just get stuff done? I don’t have the answer for you in this blog post, but I do have something else.

Here’s what I did.

For 3 weeks I paid close attention why things took longer than we expected them in our team’s day to day project work. 

Here’s what I found.

The results will shock you. (Narrator: No they won’t)

Without further ado. The list of “why things take longer than we think”:

- We spent a lot of time waiting
    - Waiting for CloudFormation to deploy (!!)
    - Waiting for CloudFormation to fail creating resources after moving them
    - Waiting for slow integration tests to finish
    - Waiting for code to finish running (slow profiling code)
    - Waiting for tests to run to completion
    - Waiting for other teams and/or bug fixes to be merged in
    - Waiting for clarity on what to work on (tickets not workable/scoped yet)
    - Waiting for other ticket to merge in first
    - Waiting for sign-off from other team
    - Waiting for other team on a bug fix
- We did not follow the process and that resulted in some waste:
    - One ticket turned out to be not necessary
    - One ticket turned out more difficult than anticipated
    - One ticket turned out to need more clarification and discussion
- Things “suddenly” started breaking
    - S3 starts failing (403 access denied in end-to-end tests)
    - Service connections start failing (can not assume role)
    - Python environments breaking after doing a fresh install (docker not building on mac, etc.)
    - Master deployments breaking (deployments randomly fails)
    - Tests failing because they were skipped in the pipeline and now diverged
    - Having to update team dependencies (changing contracts)
    - Selections package didn’t work, thought it was fixed, broke again
- We spent time debugging
    - Debugging inside docker containers (trial and error)
    - Debugging in the wrong place (docker errors were too obscure)
- We missed unforeseen work
    - New work validation (compression algorithm analysis)

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
    