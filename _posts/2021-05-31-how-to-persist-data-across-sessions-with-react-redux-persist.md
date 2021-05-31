---
title: "How to persist data across sessions in react native with redux-persist" 
date: 2021-05-31
categories:
  - blog
toc: false
toc_sticky: false
tags:
  - blog
  - react-native
header:
  teaser: "/assets/2021-05-31-how-to-persist-data-across-sessions-with-react-redux-persist/teaser-800x430.png"
---

In this blog post I'll show you how to persist your data across sessions in react native using [`redux-persist`](https://github.com/rt2zz/redux-persist).

In this blog post I assume that you: 

* have a working react native app
* you have a working redux store with a root reducer
* want to learn how to persist data across sessions

Let's get started!

## 1. Setup

We first have to install `redux-persist`.

```bash
npm install redux-persist
```

And we also have to install `async-storage`.

```bash
npm install @react-native-community/async-storage
```

## 2. Changing your store configuration

After installing, the second thing we have to do is update the file that has our redux store configuration.

Mine is very simple and looks like this:

```js
import { createStore } from 'redux';
import rootReducer from './reducer';

const store = createStore(rootReducer);

export default store;
```

And this is what it looks like after:

```js
import AsyncStorage from '@react-native-community/async-storage'; // 1. import AsyncStorage
import { persistStore, persistReducer } from 'redux-persist'; // 2. import persistStore and persistReducer

import { createStore } from 'redux';
import rootReducer from './reducer';

// 3. create a persistConfig and pass AsyncStorage explicitly for storage
const persistConfig = { 
    key: 'root',
    storage: AsyncStorage 
  }

const persistedReducer = persistReducer(persistConfig, rootReducer); // 4. create a persistedReducer
const store = createStore(persistedReducer); // 5. create persisted store
const persistor = persistStore(store) // 6. create the store persistor

export default { store, persistor }; // 7. export both of them
```

## 3. Wrap your `App` in a `PersistGate`

The third and last things that we have to do is wrap our `App` component in a `PersistGate`.

Before:

```js
import store from './redux/store';
import {Provider, useSelector, useDispatch} from 'react-redux';

// ...

export default function App() {
  return (
    <Provider store={store}>
      ...
    </Provider>
  );
}
```

And this is what it looks like after wrapping the contents of `Provider` with
the `PersistGate` with the `persistor` as the argument. Optionally, we can add a
`loading` component.

```js
import { PersistGate } from 'redux-persist/integration/react'
import {Provider, useSelector, useDispatch} from 'react-redux'
import { store, persistor } from './redux/store';

// ...

export default function App() {
  return (
    <Provider store={store}>
      <PersistGate loading={null} persistor={persistor}>
        <NavigationContainer>
          <Tab.Navigator>
          // ...
          </Tab.Navigator>
        </NavigationContainer>
      </PersistGate>
    </Provider>
  );
}
```

After saving everything I ran into this error.

```js
undefined is not an object react native redux persist
```

![](/../assets/2021-05-31-how-to-persist-data-across-sessions-with-react-redux-persist/2021-05-31-10-58-13.png)

Which I fixed by removing the `default` keyword here:

```js
export default { store, persistor };
```

Into this:

```js
export { store, persistor };
```

After which everything worked!

That's it!

Now your redux data persist across sessions. Have fun!

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
  <label for="mce-EMAIL">Liked this article and want to hear more? Join 40+ others and subscribe!</label>
  <input type="email" value="" name="EMAIL" class="email" id="mce-EMAIL" placeholder="email address" required>
    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
    <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_92fe86c389878585bc87837e8_50543deff9" tabindex="-1" value=""></div>
    <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button"></div>
    </div>
</form>
</div>
<!--End mc_embed_signup-->
