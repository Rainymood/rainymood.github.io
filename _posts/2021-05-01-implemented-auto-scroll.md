---
title: "How to auto-scroll to a focused TextInput in a ScrollView" 
date: 2021-04-26
categories:
  - blog
toc: false
toc_sticky: true
tags:
  - blog
  - javascript
header:
  teaser: "/../assets/2021-05-01-implemented-auto-scroll/auto-scroll-demo.gif"
---

I couldn't come up with a more catchy name so this is it! 
In this blog post I'll show you how to **auto-scroll to a focused `TextInput` in a `ScrollView`**. 

## Problem

What I'm working on right now is a clone of this app called [3 good things](https://apps.apple.com/us/app/three-good-things-a-happiness-journal/id1242079576). The idea behind 3 good things is that writing down three things that you are grateful for every day boosts your mood and mental wellbeing.

Anyway, that's not the main point. The main point is that the app has a neat feature which makes your screen auto-scroll to whatever input you are focusing, demonstrated here:

<img src="/../assets/2021-05-01-implemented-auto-scroll/3-good-things-demo.gif" width="250" />

So... how do we build this? 

## Solution

I spent *so* much time on this and the solution turned out to be *really* simple: instead messing with `ScrollView` and `KeyboardAvoidingView`, just use [`KeyboardAwareScrollView`](https://www.npmjs.com/package/react-native-keyboard-aware-scroll-view):

```js
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view'

<KeyboardAwareScrollView extraHeight={120}>
  <Card/>
  <Card/>
  <Card/>
  <Card/>
  <Card/>
  <Card/>
</KeyboardAwareScrollView>
```

## Result

And this is what you get:

<img src="/../assets/2021-05-01-implemented-auto-scroll/auto-scroll-demo.gif" width="250" />

Notice that nothing happens when you focus the top input, but when you focus the
bottom input it automatically scrolls with you. Nice.

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
