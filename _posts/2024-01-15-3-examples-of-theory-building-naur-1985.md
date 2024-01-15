---
title: "3 examples of theory building"
date: 2024-01-15
tags:
# Blog or how-to
- blog

# Work or personal?
- work

# Big themes that I write about
- systems

# Programming languages/Cloud
- meta programming

categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2024-01-15-3-examples-of-theory-building-naur-1985/thumbnail.png"
---
<!-- ctrl + alt + v -->

<!-- Checklist:
Title = insight
Interesting 1st sentence
Short and concise -->

<!-- Do the most annoying thing first: thumbnail creation -->

<!-- 1. interesting hook -->
I have been reading this paper [Programming as Theory building (1985) by Naur](https://pages.cs.wisc.edu/~remzi/Naur.pdf) and I have to say it is very interesting. 

![](/../assets/2024-01-15-3-examples-of-theory-building-naur-1985/2024-01-15-23-15-55.png)

What I like about this paper is that it puts programs and code in a new perspective for me. Before reading this paper I always thought that code was the most sacred thing and the objective truth that we could all agree on. Now that I've read this paper I am starting to think a bit differently.

The main premise of the paper is that it is not the program (the code) that is central, but that it is the *theory* (sort of like the mental model) of the programmers writing the program (code) that is *actually* central. 

All that programmers do is solve real world problems with code. What this means is that programmers have a theory (mental model) of the problem in their head and how to solve it. The code is merely an expression of this mental model. To write good code and to have others write good code is then an exercise in trying to shape, agree, and collaborate on this theory. 

I use the word theory quite casually here, but it has a very subtle meaning that I honestly can not fully explain. But what I got from the paper is that the theory that is mentioned here means that one has an idea, a sort of mental model, about the world which allows you to reason with it, to change it, to modify it, to play around with it. In that sense it is a bit more broader and abstract than say some physics laws. 

The important piece of this theory is that it allows you to intuit where to change a system if a change is required. One thing that the paper states (back in 1985) is that the real only constant thing is change. The world changes constantly and so programs are forced to change as well. The programmers then working on the code must also know how to change the program in ways. This is the key benefit of having this theory in mind over just looking at the code. Having this theory in mind allows you to understand how you should change the code if future requirements come in. 

### Exhibit 1

> It's like the joke about the plumber who just whacks a pipe with a hammer to fix a clog and charges 200 dollars. the client protests, saying he should only charge 5 for such a simple fix. the plumber itemizes the bill - 5 for hitting the pipe, 195 for knowing where to hit it.

You're not paying for the labour of the plumber, but for his theory (mental model) that allows him to understand where to modify the system (whack a pipe)


### Exhibit 2

![](/../assets/2024-01-15-3-examples-of-theory-building-naur-1985/2024-01-15-23-05-16.png)

> FIGURE 1.11.The Designer’s Model, the User’s Model, and the System Image. The designer’s conceptual model is the designer’s conception of the look, feel, and operation of a product. The system image is what can be derived from the physical structure that has been built (including documentation). The user’s mental model is developed through interaction with the product and the system image. Designers expect the user’s model to be identical to their own, but because they cannot communicate directly with the user, the burden of communication is with the system image.

It's the designers job to try and create a shared understanding through with the user through clever design. This is like collaborating on a project but on hard mode. The user can only see the product and documentation and needs to build a theory with just that.

I found this example in *The Design of Everyday Things* by Don Norman.

### Exhibit 3

The last example that I want to give is about the saying "The map is not the territory." In a sense a map is literally a projection of the territory, but it is not the same. Only when the generals all understand the map and how the actual territory diverges from the map, it can really be useful. Would it be possible to state, in more general terms that, the program is not the solution? The map (projection) is not the territory (reality). The program (projection) is not the solution (reality)? Maybe.

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
    