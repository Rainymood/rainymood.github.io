---
title: "Programming exercise: reading in environmental variables with dotenv"
date: 2020-10-22
categories:
  - blog
tags:
  - javascript
  - exercise
  - programming
header:
  teaser: "/assets/2020-10-22-exercise-dotenv/teaser.png"
---

Programming, as a craft, is funny. Compared to other crafts, like
professional musicians, programmers don't seem to deliberately practice their
craft. 

I would argue that it is pretty noncontroversial to say that if you want to get
better at something, you must practice. So if we want to become better
programmers, we must practice programming!

In this exercise you learn how to read in a single environmental variable and
output its contents to stdout. Repeat 5 times.

# Exercise

Exercise: 

**Write a plain JavaScript file that reads in an environmental variable from a `.env` file using the dotenv library**.

Detailed instructions: 

* Create a new folder called `practice-dotenv`
* Enter the folder `practice-dotenv`
* Install `dotenv` with `npm`
* a new `.env` file and populate it with the variable `FOO=BAR`
* Create a new file `main.js` and have it read in the variables in `.env` using the `dotenv` library

# Solution 

![](/assets/2020-10-22-exercise-dotenv/dotenv.gif)

```bash
mkdir practice-dotenv
cd practice-dotenv
npm i dotenv
```

Create a new file `.env` with these contents. Notice that there are no spaces
around `=`.

```bash
FOO=BAR
```

Create a new file called `main.js` with the following contents. 

```js
require('dotenv').config();
console.log(process.env.FOO);
```

When we run it, this should be the expected output. 

```bash
$ node main.js
BAR
```

# Closing remarks

This exercise sounds trivial. Perhaps it is. Yet, if it is really this
trivial, can you do it? Can you do it without peeking at the solution?

Do you really know how to do this? Or do you *think* you know it? 

The first time I did this exercise without looking at the solution I tried to
`console.log(NAME)`! This is wrong! The correct solution is
`console.log(process.env.NAME)`. I thought I knew, but I didn't! This
exercise poked a hole right through my veil of ignorance.

Please try out the exercise and let me know in the comments what you think of
it! I'd love to hear your feedback on this piece.

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
  <label for="mce-EMAIL">Liked this article and want to hear more? Join 53 others and subscribe!</label>
  <input type="email" value="" name="EMAIL" class="email" id="mce-EMAIL" placeholder="email address" required>
    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
    <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_92fe86c389878585bc87837e8_50543deff9" tabindex="-1" value=""></div>
    <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button"></div>
    </div>
</form>
</div>
<!--End mc_embed_signup-->