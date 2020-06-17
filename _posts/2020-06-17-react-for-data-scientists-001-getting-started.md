---
title: "React for data scientists part 1: Getting started" 
date: 2020-06-17
categories:
  - blog
tags:
  - react
  - data-science
  - tutorial
header:
  teaser: "/assets/2020-06-17-react-for-data-scientists-001-getting-started/teaser.jpg"
---

With modern frameworks like React, Angular, Vue, Next.js, Gatsby, and 
Jekyll, modern web development can seem scary. However, I assure you that it
is not. In this blog post I will show you that it is very easy to get started
with [React](https://reactjs.org/). In fact, I will teach you in just 5
minutes. Here we go!

# Installation

Let's first install React. 

OK. Installing React is kind of a misnomer because React is a framework. How
to *setup* React would be more appropriate.

To setup React we need [NodeJS](https://nodejs.org/en/). So install that
first if you don't have it. Installing NodeJS gives us access to `npm` which
gives us access to `npx`.

Let's start with: 

```bash
npx create-react-app hello-world
```

`create-react-app` creates the standard cookie-cutter React project
skeleton for you. If everything runs smoothly your terminal should look
something like this.

<img src="/assets/2020-06-17-react-for-data-scientists-001-getting-started/img1.png">

# Let's run it

Follow the suggestions and run

```
cd hello-world
yarn start
```

Your default browser should pop up with this page

<img src="/assets/2020-06-17-react-for-data-scientists-001-getting-started/img2.png">

🎉 **YOU DID IT! YOUR FIRST REACT APP** 🎉

# Now lets modify it

In `src/App.js` find the function called `App()` and change the code in the `<p>` marks into something else like "Hello world"

```js
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}
```

Change that to 

```js
      ...
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Hello world!
        </p>
      ...
}
```

Save it. Now your React app looks something like this.

<img src="/assets/2020-06-17-react-for-data-scientists-001-getting-started/img3.png">

# Conclusion

That's it! Your first react app! While it doesn't do a whole lot, you sure
can be proud of yourself for taking the first step to learn React.

Modern web development can seem scary with the overwhelming amount of frameworks and
libraries. What I've learned is just to pick one of them and start builing
silly little stuff with it, learning the frameworks and terminology as you
go.

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
  <label for="mce-EMAIL">Liked this article and want to hear more?</label>
  <input type="email" value="" name="EMAIL" class="email" id="mce-EMAIL" placeholder="email address" required>
    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
    <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_92fe86c389878585bc87837e8_50543deff9" tabindex="-1" value=""></div>
    <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button"></div>
    </div>
</form>
</div>
<!--End mc_embed_signup-->
