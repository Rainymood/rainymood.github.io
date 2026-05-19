---
title: "Infrastructure thoughts"
date: 2026-05-19
tags:
- software
- systems
- software architecture
- engineering
- domain driven design

categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2026-05-19-infrastructure-thoughts/thumbnail.png"
---
<!-- ctrl + alt + v -->
<!-- cmd + alt + v -->

![](/../assets/2026-05-19-infrastructure-thoughts/2026-05-19-17-55-01.png)

Last Friday was great. I met up with Arnaud and we had tacos and crazy flavored beer called Michelada. The beer was dark and spiced with fish sauce and Worcestershire sauce. I ate some of the best tacos in my life. Then, on the terrace in the sun, we talked software architecture. Man. Life is good.

The unintelligible diagram above is the result of the brainstorm, or the beer, or a bit of both. Anyway, from the conversation I got two key takeaways that I don’t want to forget:

1. **Swapping out infrastructure should be easy.** One of the most important ideas is that we should be able to easily swap out the infrastructure for something else. For example, can we do the whole thing not with what we have now, but with files on s3, or parquets? Can we create new implementations of the interfaces and have everything work magically together? The domain dependencies should point inward, not outward. The domain logic should not know anything about the outside world. It should not know about implementation details, hence it is free to change.
2. **Think in terms of responsibilities**. Who is responsible for what? What needs to happen? How does that get computed? Who is responsible for that specific thing? Encapsulate these design decisions in modules and think hard if they are not duplicated somewhere else.

Author’s note:

I wrote this original post last summer in the sweltering heat of July. I spent 40 minutes in the hot hot metro that took me from the most southern metro station in Paris (Maison Blanche) all the way up north to Louis Blanc. The moment I popped my head out of the metro the vibe shifted, it was gritty, alive, but also very different from the chinatown that I live in myself.


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
    