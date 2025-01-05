---
title: "A Philosophy of Software Design - John Ousterhout"
date: 2025-01-05
tags:
# Blog or how-to
- blog
# Work or personal?
- work
# Start here themes
- systems
- software
- complexity
- software architecture
categories: blog
toc: true
toc_sticky: true
header:
    teaser: "/../assets/2025-01-05-a-philosophy-of-software-design-john-ousterhout/thumbnail.png"
---
<!-- ctrl + alt + v -->

I'm a big fan of the book A Philosophy of Software Design written by John Ousterhout and I've written about it before [here](), [here](), and [here](). A large part of my thinking about managing system complexity is shaped by the book.

<!-- <img src="/../assets/2024-05-03-book-notes-a-philosophy-of-software-design/2024-05-03-14-12-53.png" style="max-height: 250px">{: .align-center} -->

I wrote a summary in bullet points before [here](), but that was very unclear even to me, so below you will find a new summary of what I think are the most important parts of the book.

# Intended audience

This post is for mid-to-senior level machine learning engineers, software engineers, and data scientists that want to make a contribution beyond coding, that want to design smarter systems, and drive more meaningful impact in their org.

---

# 1. Summary

When building software systems of significant size, the main challenge is **managing complexity**.

💡 The book defines complexity as: *"Anything related to the structure of a software system that makes it hard to **understand and modify the system**"*
{: .notice--info}

Good software design is one of the tools that we can use to manage this complexity: 

* One of the biggest limits we are constantly fighting against is our ability to juggle things simultaneously in our head, i.e. our working memory. Our working memory is limited to around 7 plus minus 2 items [[1]](https://en.wikipedia.org/wiki/The_Magical_Number_Seven,_Plus_or_Minus_Two).
* Complexity is caused by dependencies and obscurities. Dependencies are a fundamental part of software development but they must be managed carefully.
* Complexity manifests itself in programs as change amplification (changes becoming harder to make) and cognitive load (having to juggle more things in our heads when making changes)
* The golden rule is to Pull Complexity Downwards. Aim to write deep modules. Deep modules are modules with a simple interface but deep and complex implementation. These modules encapsulate complexity. Try to have each module represent a design decision and encapsulate that information only in that module.
* Test-Driven Development (TDD) is good but lacks a fundamental feedback loop that drives the system towards a better design over time.

---

# 2. The nature of complexity

Ousterhour writes that complexity manifests itself in the following ways in a program:

1. Change amplification: A seemingly simple change requires code modifications in many different places. Because of this it becomes harder and harder to make changes to the system as the system grows.
2. Cognitive load: A programmer needs to know too many things (relative to our working memory capacity) to make changes and modify the program.

---

# 3. What causes complexity

Ousterhout identifies two main causes of complexity:

1. Dependencies: Dependencies are a fundamental part of software development so they can not be completely eliminated, but it can be and must be managed to a certain degree, otherwise you end up with the well-known [big ball of mud](https://blog.codinghorror.com/the-big-ball-of-mud-and-other-architectural-disasters/).
2. Obscurity: When important information is not obivious this creates unknown unknowns which contribute to a higher cognitive load.

---

# 4. How to fight complexity

Ousterhout suggests two ways of dealing with complexity:

1. Eliminating complexity: The first way is to eliminate complexity by making your code as obvious as possible.
2. Encapsulating complexity: The second way is to encapsulate complexity so that you are only exposed to the complexity of the interface of the module instead of the implementation. We effectively hide the complexity of the module by providing a simple interface coupled with a powerful implementation.

---

# 5. Code should be obvious to the reader

Code is read more often than it is written. 

Thus, code should be more obvious to the reader than to the writer. If the reader does not find the code clear, then the code and not the reader is often times in the wrong.

Even more important is that the interface of the module is obvious to the reader. Why? Because the interface is what other modules will depend on. Managing `foo(a)` is easier than managing `foo(a,b,c,e)`.

---

# 6. Deep modules are less complex than shallow modules

Aim to write deep modules, modules with powerful functionality but a simple interface.

The opposite of a deep module is a shallow module. A shallow module is a module with a large or complex interface but not so much depth.

> This is one of the core themes in the book. A software system is usually decomposed into a collection of modules that are relatively independent. Modules inevitably have dependencies between them - they work together by calling each other, and therefore must know about each other. In order to manage these dependencies, we think about a module in two parts: an interface (what the module does), and an implementation (how it does it). [source](https://www.mattduck.com/2021-04-a-philosophy-of-software-design.html)

This is indeed one of the core themes of the book that is worth driving home over and over again. In order to manage the growing complexity of any codebase we must make deep and powerful modules with simple interfaces.

Yes, there is a lot of complexity, but this is encapsulated behind a simple interface that can be depended on by other modules. *This* is the trick that allows us to manage complexity, by encapsulating it.

---

# 7. Modules should represent design decisions

You can create deep modules by using the information hiding principle [[1]](): Modules should encapsulate a few pieces of knowledge that represent design decisions.

The opposite of this is information leakage: Design decisions that are spread or duplicated across multiple modules. This creates change amplification or coupling because making a change in the design decision will force you to make changes in both multiple modules.

Information can also leak through the implicit interface like having to know about the file format, or the order in which things should be executed.

In practice, the main culprit we see is temporal decomposition: using the temporal flow of information/data to split up modules. For example in a machine learning setting this could lead to the following modules: train dataset creator module, training module, test dataset creator module, test evaluation module. The problem is that both the train and test dataset creator module need to know the same thing, this design decision should be in one single module: the dataset creator module.

---

# 8. Pull complexity downwards

The golden rule is this: **Pull complexity downwards**.

It is more important for a module to have a simple interface than a simple implementation. In other words, modules should be deep.

Should you let your users grapple with the complexity of your module or should you put it inside the module? The answer is almost always to pull the complexity downwards and handle it inside the module. 

Strive to make life as easy as possible for your users, even if it makes your own life harder. It is much more important for your module to have a simple interface than to have a simple implementation.

The example given in the book is configuration parameters. In general, configuration parameters should be set to good defaults so that the caller does not need to set them. Do you really think that the caller can make better decisions on what are good configuration parameters? Or are you just lazy and you don't want to do it yourself? Strive to make life easier for your users, even if this means taking on a bit of suffering for yourself.

---

# 9. TDD is good but does not not lead to good design

> "The problem with test-driven development is that it focuses on getting specific features working, rather than finding the best design." Ousterhout argues that the unit of development should be abstractions rather than features, and that once you discover the need for an abstraction, you should design it all at once. [source](https://www.mattduck.com/2021-04-a-philosophy-of-software-design.html)

TDD never encourages you at any point in the process to step back and improve your design. You can merge in 10 pull requests that are completed features and that are well-tested, but your design could slowly get worse with each merge.

There is no feedback loop in TDD that forces you to look at and improve your design.

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
    