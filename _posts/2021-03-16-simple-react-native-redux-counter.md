---
title: "Simple React Native Redux counter example"
date: 2021-03-16
categories:
  - blog
tags:
  - tutorial
  - react-native
header:
  teaser: "/../assets/2021-03-16-simple-react-native-redux-counter/teaser.gif"
---

If you are learning [React Native](https://reactnative.dev/) and [Redux](https://redux.js.org/) and still really don't *understand* Redux try looking at this simple counter app that I made. This app aims to clearly illustrate the key concepts of Redux (store, actions, reducers) in a very small toy project. 

This is what it looks like:

![](/../assets/2021-03-16-simple-react-native-redux-counter/demo.gif)

The code can be found [here](https://github.com/Rainymood/react-native-redux-counter).

Main idea to keep in the back of your head: 

* Instead of storing the data inside of our components we basically extract the data to an external store (our `store`) 
* We then communicate with this store through an "API" which is the Redux language, or in our case the `react-redux` library
* The only way you can change the store is by dispatching an action to your reducer
* Your reducer then decides how to change the state, depending on the action you gave it (ex. increment counter)

Key concepts: 

* **Store**: Your store is a plain JS object that is read-only. The only way to change the store is through reducers.
* **Actions**: Actions are JS objects that have a `type` field, nothing more, nothing less.
* **Reducers**: Reducers are functions that take in the state and an action and return back the new state. A reducer must be a pure function, that is, it shouldn't have any side effects. In essence a reducer can be formulated like this `(state, action) => state`

This is what I learned:

* Use `useSelector` to grab values from the store
* Use `useDispatch` to dispatch actions to your reducer
* A Redux app only really has one reducer, the `RootReducer`
* Wrap your whole app in a single component so you can wrap *that* in a `Provider` component to give access to the store
* When importing your **Action Creators** make sure to import them like this `{ addTodo }`

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
