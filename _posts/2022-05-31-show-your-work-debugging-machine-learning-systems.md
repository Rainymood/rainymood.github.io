---
title: "Show your work: Debugging Machine Learning Systems"
date: 2022-05-31
tags:
- blog
- jekyll
- machine-learning
- show-your-work
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2022-05-31-show-your-work-debugging-machine-learning-systems/thumbnail.png"
---

![](/../assets/2022-05-31-show-your-work-debugging-machine-learning-systems/2022-05-31-15-23-09.png)

This graph has been keeping me busy for the last couple of weeks, and not in a good way.

This graph shows the area under the curve of one of our core algoriths in the platform at [Snappet](). 

You can see a stable period in the middle and then suddenly performance degrades by a lot. This is bad, very bad.

If you know anything about machine learning you know we are in trouble, an AUC of 0.50 is pretty bad. We had to drop our work and get this fixed asap. This was quite a multi-team effort to get this fixed. 

This is what we learned.

**Lesson 1: Monitor algorithmic performance.**
The biggest thing we learned from this is that you should always monitor your
algorithm's health.  How do you otherwise know that your performance has dropped
in production if you don't monitor it? This is impossible! Madness!  Track your
algorithm's health metrics and establish boundaries that alert you when your
metrics drop below these thresholds. If we had this monitoring, we
would've spotted this much earlier.

**Lesson 2: Debugging interacting systems is hard.** 
The system that this AUC belongs to does not work in isolation.  This is one of
the internal metrics of a system (continuous calibration) setting difficulty
values for exercises in the platform.  We have another system that also sets
difficulties in the platform (default difficulty).  These two systems are
intertwined and work together creating a lot of interacting and moving pieces
making this hard to debug.

**Lesson 3: Communicate proactively to stakeholders.**
It's easy to get lost in fixing things, debugging things, and following complex
logic.  But you must not forget to come up for air every once in a while to
update the stakeholders, *even if you haven't completely fixed the issue*.
Because if you wait with your first update until you fix the issue completely,
then from their perspective you've just been completely silent.  So, don't wait
too long with updating your stakeholders, keep them in the loop by communicating
proactively.

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
