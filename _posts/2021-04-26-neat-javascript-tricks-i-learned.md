---
title: "Three JavaScript tricks I learned today"
date: 2021-04-26
categories:
  - blog
toc: true
toc_sticky: true
tags:
  - blog
  - javascript
header:
  teaser: "/../assets/2021-04-26-neat-javascript-tricks-i-learned/teaser800x430.png"
---

Today I learned some cool "tricks" (uhmm... fundamentals...) in JavaScript. 

In this blog post I'll show you how to: 

* check if at least one value is false in an array
* check if all values are false in an array
* find an element in an array

# Trick 1: How to check if at least one value is false in an array

To check whether at least one value in the array is `false` you can use [`some()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some):

> The `some()` method tests whether at least one element in the array passes
the test implemented by the provided function.  It returns true if, in the
array, it finds an element for which the provided function returns true;
otherwise it returns false.  It doesn't modify the array.

```js
const array = [false, true, true];

// check whether any element is false
array.some(x => x == false); // true
```

Try it out by clicking [here](https://replit.com/@Rainymood/ConstantOrdinaryGenerics#index.js).

# Trick 2: How to check if all values are false in an array

To check if all values are false in an array you can use [`every()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/every):

> The `every()` method tests whether all elements in the array pass the test
implemented by the provided function.  It returns a Boolean value.

```js
const array1 = [false, false, false];
array1.every(x => x == false); // true

const array2 = [false, false, true];
array2.every(x => x == false); // false
```

Try it out by clicking [here](https://replit.com/@Rainymood/SuperbTremendousRedundantcode#index.js).

# Trick 3: How to find an element in an array

To find an element in an array based on some condition you can use [`find()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find):

> The `find()` method returns the value of the first element in the provided
array that satisfies the provided testing function.  If no values satisfy the
testing function, undefined is returned.

```js
const array1 = ["2021-04-25", "2021-04-26"];
const today = "2021-04-26";

// Find item that returns true
console.log(array1.find(item => item == today)); // "2021-04-26"
```

Note 1: Only matches the first match.

Note 2: If you need to find the index use [`findIndex()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/findIndex).

# Bonus: Get today's string in YYYY-MM-DD format

Here's a nice bonus. I also had to get today's date in the format of `YYYY-MM-DD` (ex. `2021-04-26`) and this is how you do that:

```js
const today = new Date()
const todayString = today.toISOString().slice(0,10);
```

# Conclusion

That's it! That's all I wanted to share today. By writing these down I hope I remember them better for next time. I call these things tricks but they are more like fundamentals, but hey, we all have to start somewhere!

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
