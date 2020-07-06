---
title: "Learning TypeScript - The basics" 
date: 2020-07-06
categories:
  - blog
tags:
  - blog
  - typescript
  - javascript
  - learninpublic
header:
  teaser: "/assets/2020-07-04-typescript-for-dummies-1/teaser.jpg"
---

For a new project at work I will have to lead a project in
[TypeScript](https://www.typescriptlang.org/). Here comes the kicker: I've
never worked with TypeScript.

Thankfully, I have worked with JavaScript (ES6 in particular) and React
before. I am no stranger to JavaScript and all its quirks. In fact, I
actually took up an interest in TypeScript but never managed to build
anything substantial with it other than toying around with it a bit.

In this blog post I will go over the basics of TypeScript as I have learned
them thusfar. I will use this experience to learn in public about TypeScript
so you can join me on my adventure!

## What is TypeScript? 

Concisely put, TypeScript is a strict superset of JavaScript. 

<img width="50%" src="/assets/2020-07-04-typescript-for-dummies-1/CamScanner 07-04-2020 10.12.19_1.jpg">

This means that all JavaScript is also valid Typescript, but TypeScript comes
with additional features:

* Strongly-typed variables 
* Object-oriented programming

<img width="60%" src="/assets/2020-07-04-typescript-for-dummies-1/CamScanner 07-04-2020 10.12.19_2.jpg">

TypeScript adds strong-typing features to JavaScript like other programming
languages like Java and C++. Furthermore, TypeScript also adds the ability to
write more object-oriented code with classes and interfaces.

## Getting started

Getting started with TypeScript is ridiculously simple. Just install it with `npm`. 

```bash
$ npm install -g typescript
/usr/local/bin/tsc -> /usr/local/lib/node_modules/typescript/bin/tsc
/usr/local/bin/tsserver -> /usr/local/lib/node_modules/typescript/bin/tsserver
+ typescript@3.9.6
added 1 package from 1 contributor in 2.442s
```

If everything installed successfully you should be able to check the version. 

```bash
$ tsc -v
Version 3.9.6
```

Now you can compile any `.ts` file with 

```
tsc filename.ts
```

## Variables

Let's continue with one of the main features of TypeScript: strong typing. Unlike in JavaScript, we can define the type of our variables as being a number, string, boolean, etc. 

<img width="60%" src="/assets/2020-07-04-typescript-for-dummies-1/CamScanner 07-04-2020 10.12.19_4.jpg">

The syntax for this is `let <varname>: <type>`. Here are some more examples of strong typing in TypeScript.

```
let name: string;       // strings
let age: number;        // numbers
let isChecked: boolean; // boolean
let data: any;          // any type
let array: number[];    // array of numbers
```

## Classes

TypeScript also adds classes! I knew that ES6 already has classes, but this
is a huge step over the original ES5, of course.

Personally I am not that much into object-oriented programming I've heard
good things about this from others. So, yay for classes?

<img width="60%" src="/assets/2020-07-04-typescript-for-dummies-1/CamScanner 07-04-2020 10.12.19_6.jpg">

## Access modifiers

Next up we have another feature that can be grouped under the object-oriented
features that TypeScript has: access modifiers.

<img width="60%" src="/assets/2020-07-04-typescript-for-dummies-1/CamScanner 07-04-2020 10.12.19_5.jpg">

TypeScript allows for three different access modifiers: 

* Public - Allow access outside of class
* Protected - Allows access from within its class and its derived classes. 
* Private - Allow access from within class

Basically members (properties and methods) of TypeScript are public by
default. Protected members can be accessed only from the same class and its
derived class. Private members can only be accessed from the same class. 

This example illustrates the protected access modifier. 

```js
class Car{
    protected name: string;
    constructor(name: string) { this.name = name; }
}

class Mercedes extends Car{
    constructor(name: string) { super(name); }
    }

    public welcomeMessage() {
        return `Hello, This is my ${this.name}.`;
    }
}

let myCar= new Mercedes ("NightRider", 4);
console.log(myCar.welcomeMessage());  // returns: Hello, this is my Nightrider. 
console.log(myCar.name); // returns: Error!! , Property 'name' is protected and only accessible within class 'Car' and its subclasses.
```

The reason we can not call `myCar.name` directly is because the member `name`
is protected. This means that we can only access it from within its class or
derived classes.

## Conclusion

This blog post is an introduction into TypeScript and what makes TypeScript
different from JavaScript. Some of these features include:

* Strong-typing for variables
* Object-oriented features
  * Classes
  * Access modifiers

I am personally most excited about the possibility of strong-typing my
variables. A lot of my previously made bugs could have been avoided with
this.

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
