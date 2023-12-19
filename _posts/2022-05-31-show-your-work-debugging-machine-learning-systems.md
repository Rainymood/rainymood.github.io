---
title: "Show your work: The nastiest bug I've ever seen in an ML system"
date: 2022-06-10
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
published:
  false
---
<!-- ctrl + alt + v -->

This week I want to share with you what has been keeping me busy for the last couple of weeks (and not in a good way). 

![](/../assets/2022-05-31-show-your-work-debugging-machine-learning-systems/2022-05-31-15-23-09.png)

This graph shows the area under the curve (AUC) metric of one of our core algorithms [Snappet](https://us.snappet.org/). This graph can be thought of as the **algorithmic health of our platform**.

The 5 coloured lines are the 5th, 25th, 50th, 75th, and 95th percentile lines of the metric. Having it drop below 0.55 is bad (highest horizontal blue line), but having it drop below 0.50 (lowest horizontal blue line) is even worse. 

We start at the black line. The period before the black line is good, stable, but then suddenly, like magic, it starts sliding down. The metric starts degrading. *Oh shit. What the hell is going on?*

The metric degraded so much that the green line (the median) had an AUC below 0.55 (the highest blue line). If you know anything about machine learning you can understand that this is pretty bad. If you don't know anything about machine learning just take it from me, that's bad. 

It got so bad that this was an all-hands on deck type of situation and we pulled some teams together to fix this, ASAP. 

I'm very glad I can finally send out this post because we finally fixed it! I will spare you all the details but this was honestly the **nastiest dirtiest bug that I've ever seen**.

First, we thought it had something to do with the difficulties of the exercises in our platform (we are an edtech company). We reset the difficulties but that didn't seem to fix the issue. 

Then we thought it had something to do with the actual algorithm. We went through the algorithm, fixed what we thought was wrong, but that also didn't fix it. 

Then after a painstaking investigation, one of our engineers figured out that **it was an external library that was flipping some of our ground truths while reading in the data (0 to 1s and 0s to 1s)**. 

Note that it only flipped *some* of the ground truths. This is what made it so incredibly difficult to track down. 

You can view the github issue on said library that one of our senior architects made [here](https://github.com/aloneguid/parquet-dotnet/issues/168). 

This is the craziest bug I've seen in my career thus far. 

Anyway, here are some lessons that I (personally) learned from this:

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
