---
title: "Working together with interfaces"
date: 2024-01-16
tags:
# Blog or how-to
- blog

# Work or personal?
- work

# Big themes that I write about
- engineering

# Programming languages/Cloud
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2024-01-16-working-together-with-interfaces/thumbnail.png"
---
<!-- ctrl + alt + v -->

<!-- Checklist:
Title = insight
Interesting 1st sentence
Short and concise -->

<!-- Do the most annoying thing first: thumbnail creation -->
Successful collaboration relies on shared interfaces.

![](/../assets/2024-01-16-working-together-with-interfaces/2024-01-16-20-25-09.png)

Currently, I'm part of a project in my organisation involving three teams: the mlops team (my team), the data team, and the dashboard team. 

The data team creates the model, we handle hosting it in our infrastructure, and the dashboard team takes care of visualisation. To make this collaboration work, we need to interact with both teams, consuming and hosting the model, and providing its output to the dashboard team.

The only real way of making this collaboration go smoothly is by establishing a clear interface. We need to align with both teams (the data team and the dashboard team) in what we expect to give them and what we expect in return.

For example, one such agreement could look something like this:
* We will put files on `s3://{env}-{region}-service/foo/bar/things.json` 
* With `things.json` being valid `json` with the following format: `{String<Name>: String<<List[Int]>>}`. 

Agreeing on this interface provides a clear point of separation, allowing both teams to work in parallel because you can pretend you get the output agreed upon in the interface (mock it, fake it, whatever). The important thing is that your interface need not be perfect from the start, but agreeing on one is the first step in decoupled collaboration.

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
    