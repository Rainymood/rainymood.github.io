---
title: "Book notes: A philosophy of software design"
date: 2024-05-03
tags:
# Blog or how-to
- blog
# Work or personal?
- work
# Big themes that I write about
- engineering
- software architecture
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2024-05-03-book-notes-a-philosophy-of-software-design/thumbnail.png"
---
<!-- ctrl + alt + v -->

<!-- Checklist:
Title = insight
Interesting 1st sentence
Short and concise -->

If you want to write better code, read this book by John Oosterhout: A Philosophy of Software Design.

![](/../assets/2024-05-03-book-notes-a-philosophy-of-software-design/2024-05-03-14-12-53.png)

The book is short, it reads easily, and it contains new insight every time you read it. 

This is actually my second time reading it. 

After having faced a different set of challenges at work I got wildly different insights from this read compared to the first time I read it. 

Here's my cliff notes of the book in bullet points. [1]

**Introduction**

- Software is about complexity
- Two ways of dealing
    - Eliminate complexity
    - Encapsulate complexity
- Modular design: be able to work on a system without being exposed to all complexity at once
- Goal: recognize complexity and provide tactics to solve
    - Ex. classes should be deep
- Practice: recognize red flags

**Complexity**

- Crucial skill: the ability to recognize complexity
- **Complexity is anything related to the structure of a software system that makes it hard to understand and modify the system**
- Complex ≠ large, a system can be large and sophisticated (”complex”)  but easy to change so not complex
- Three manifestations of complexity:
    - Change amplification
    - Cognitive load
    - Unknown unknowns
- Two causes of complexity:
    - Caused by dependencies
    - Caused by obscurity
- Complexity accumulates incrementally from dependencies and obscurities
- Complexity results in change amplification which accumulates more complexity etc.

**Working code isn’t enough**

- Tactical versus strategic programming
- Invest 10-20% in design and refactoring and system design
- Good design doesn’t come for free, you have to fight for it

**Modules should be deep**

![](/../assets/2024-05-03-book-notes-a-philosophy-of-software-design/2024-05-03-14-24-08.png)

- Modular design: face only part of the complexity at a time
- Modules can be anything: services, classes, interfaces, subsystems
- The goal of modular design is to minimize dependencies between modules
- Module has two things
    - Interface: what
    - Implementation: how
- When working with modules you should know the interface and implementation of the current module but *only* the interface of all surrounding modules
- The best modules are those whose interfaces are simpler than the implementations
- Interface two parts
    - Formal: encapsulated in the function signature (explicit)
    - Informal: high level things not captured in code (i.e. the understanding that a file gets deleted, constraints on usage of the class)
- Abstraction: simplified view of entity that omits unimportant details
- For a module, its interface is an abstraction from its implementation
- **The best module are deep, they have a simple interface yet provide powerful functionality**
- A deep module is a good abstraction because it only a small fraction of its internal complexity is visible to users
- Hide complexity by separating interface and implementation from the rest of the system

**Information hiding**

- Create deep modules using **information hiding**: modules should encapsulate a few pieces of knowledge which represent design decisions
- The opposite is **information leakage**: design decisions that are duplicated across multiple modules.
- This creates coupling because any change in the design decision needs be reflected in more than one place
- Information can be leaked even if not through the interface (ex. needing to know about file format)
- Temporal decomposition
- When designing modules, focus on the knowledge needed, not the order of the steps in which they occur
- Information hiding and deep modules go hand in hand
- Think about what information is needed to perform the task and not the order of tasks
- Design each module to encapsulate one or more of these pieces of knowledge

**General purpose modules**

- Trade-off: Investing time and effort to make it more general now versus hard to predict future uses
- Solution: make modules somewhat general
- Module’s functionality should reflect current uses but the interface should support future uses
- Generality leads to deeper modules

**Different layer different abstraction**

- Red flag: pass-through methods
- Red flag: pass-through variables
- Every layer in the architecture should have a different abstraction

**Pull complexity downwards**

- Golden rule: pull complexity downwards
- Should you let the user grapple with the complexity, or put it in the module? The answer is always to pull it downwards and handle it yourself
- Most module have more users than developers, so it is natural for them to suffer more
- Strive to make life as easy as possible for your users, even if it makes your own life harder
- It is more important for a module to have a simple interface than a simple implementation
- It is tempting to act the other way around
- When designing modules, look for opportunities to take a little bit of suffering upon yourself to make life easier for your users

**Better together or better apart**

![](/../assets/2024-05-03-book-notes-a-philosophy-of-software-design/2024-05-03-14-23-50.png)

- Fundamental question: Given two pieces of functionality should they be together or apart?
- The goal is to minimize total system complexity
- Subdivision works for reducing complexity, but also adds complexity in the form of more components
- Bring together if information is shared
- Bring together if it will simplify the interface
- Bring together to eliminate duplication
- Red flag: Special-general mixture
- Red flag: Repetition
- Split up methods only if it reduces total system complexity
- Most developers split methods too much
- Each method should do one thing and do it completely
- Red flag: Conjoined methods that you need to see together to understand
- Pick the structure that hides the best information, has the fewest dependencies, and the deepest modules

[1] The fact that I put this blog post in bullet points is actually somewhat funny imho because it violates one of the principles mentioned in the book. 

The principle it violates is the "Pull complexity downwards" principle. That principle states that you want to take suffering upon yourself to make life for your users easier. I am violating this by writing this blog post in bullet points (making life easy for myself) but harder for my readers (because what do I exactly mean with these bullet points? They make more sense for me than for you). 

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
    