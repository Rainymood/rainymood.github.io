---
title: "Reading Notes: Hexagonal, Onion & Clean Architecture"
date: 2023-03-04
tags:
- architecture
- programming
- code
- reading notes
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2023-03-04-reading-notes-hexagonal-onion-clean-architecture/thumbnail.png"
---

This is my summary of this great video [Hexagonal, Onion & Clean Architecture](https://www.youtube.com/watch?v=JubdZIdLQ4M&t=1s&ab_channel=DrawingBoxes). I love this video because to me it really captures the essence of the hexagonal architecture in a fun and entertaining way.

# N-layered architecture

![](/../assets/2023-03-04-reading-notes-hexagonal-onion-clean-architecture/2023-03-04-08-08-18.png)

# Invert the data access layer


![](/../assets/2023-03-04-reading-notes-hexagonal-onion-clean-architecture/2023-03-04-08-13-14.png)

# But how? Using Interfaces!

![](/../assets/2023-03-04-reading-notes-hexagonal-onion-clean-architecture/2023-03-04-08-16-58.png)

# Ports and Adapters

![](/../assets/2023-03-04-reading-notes-hexagonal-onion-clean-architecture/2023-03-04-08-18-21.png)

# Hexagonal architecture

![](/../assets/2023-03-04-reading-notes-hexagonal-onion-clean-architecture/2023-03-04-08-19-32.png)

# Keep domain logic independent of everything

![](/../assets/2023-03-04-reading-notes-hexagonal-onion-clean-architecture/2023-03-04-08-21-26.png)

# Increased testability

![](/../assets/2023-03-04-reading-notes-hexagonal-onion-clean-architecture/2023-03-04-08-24-51.png)

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
    