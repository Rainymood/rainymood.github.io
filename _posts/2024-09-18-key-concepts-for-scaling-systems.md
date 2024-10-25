---
title: "Key concepts for scaling systems"
date: 2024-09-18
tags:
# Blog or how-to
- blog
# Work or personal?
- work
# Start here themes
- systems
- tip


categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2024-09-18-key-concepts-for-scaling-systems/thumbnail.png"
---
<!-- ctrl + alt + v -->

There are many different tricks to build systems that scale, but they all follow the same underlying principles:

1. **Caching**: What expensive computations can we store and then serve again without recomputing them? This works both for computations but also for static website content.
2. **Decoupling producers and consumers**: Add a queue between a producer and consumer to decouple them. This provides a buffer and safety for if one of them inevitably falls over. 
3. **Separate reads from writes**: Often the read and write workload is vastly different. Can we exploit this and create a main write database and multiple follower read replicas?
4. **Horizontal scaling & load balancing**: Can we scale our systems in such a way that we can simply add more machines to handle the load? This works for both servers (autoscaling) but also for databases (sharding). This does mean that we have to balance and manage this load.

![](/../assets/2024-09-18-key-concepts-for-scaling-systems/2024-09-18-00-37-44.png)

Image is from Alex Xu's book. 

<!-- https://app.bannerbear.com/projects/POobgvMNDkxzxAYW70/templates/3g8zka5Y2OlaDEJXBY

https://www.photopea.com/ -->




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
    