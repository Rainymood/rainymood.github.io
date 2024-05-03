---
title: "How to write good code (draft)"
published: true
toc: true
toc_sticky: true
---

In this essay I try to write down everything I know about **how to write good code.**

I know that a lot of colleagues of mine, for their growth goals, are working on learning how to craft better code. And this blog post is the one I want to be able to link them to if they ask me "Hey Jan, do you have some tips to write good code?"

First, I talk about code and what exactly makes good code good. 

Here I show that:

* Code is social
* Code spends most of its time in maintenance mode
* Code needs to be easy to change

Then, I talk about **complexity** and the **philosophy** behind software design. 

Here I:

* Talk about complexity, what is it and how does it relate to software?
* Ways to reduce and harness complexity

This is largely a summary of the book A Philosophy of Software Design by John Oosterhout. 

Then, I talk about about **software architecture**, what is software architecture exactly, and what can we do with it?

Here I talk about:

* What is software architecture
* What makes a certain software architecture good? (Spoiler: it's about being easy to change)
* The Golden Rule of software architecture

The final section contains **tactics** that you can use. These are practical and specific things that you can immediately apply in your day-to-day.

# What makes good code good

![](/../assets/software/2024-05-02-11-45-02.png)

## Introduction

If we want to write good code, we must first define what we mean by good code.

There are no black and white rules, but there are some general rules of thumb I think most of us agree on.

## Code, like language, is deeply human.

> "Programs should be written for people to read, and only incidentally for machines to execute." -- Unknown

The first thing we should agree on is that **code is social**. Code is written by humans and for humans. 

This is important to align on because this means that every rule I write here about how to write good code might not translate across borders or cultures. 

Every culture is different, hence every culture will have it's own unique set of what really is good code. But maybe there are some general principles that do translate well across cultures.

## Code spends most of its time in maintenance mode

> "Code is read more often than it is written." -- Unknown

A funny thing happens when you work at any company long enough. You work on a project, write some code, you finish the project, and then a year later you actually have to revisit your old project and you wonder who wrote that piece of crap. You realize it was you who wrote it. 

This is a special case of a principle that code is read more often than it is written. Another way of framing this is that the second you write and commit the code it goes in maintenance mode. If you have a healthy project with a lifespan of 2 years and it takes around a week to write the code, that means that it spends more than 99% of the time in maintenance mode (1 week coding versus 103 weeks maintenance). Good code should be maintainable.

## The best code is no code

> ["The Best Code is No Code At All" -- Jeff Atwood](https://blog.codinghorror.com/the-best-code-is-no-code-at-all/)

The best code is no code.

If you can write less lines of code, then do it. Less lines of code means less things to maintain which means more time you can spend on every line relatively. 

Do not pride yourself into using *lines written* but instead think of it as *lines spent*. 

## The best code is a solved problem

The best code is no code (and a solved problem).

Writing code should not be the goal in and of itself.

The code exists to **solve a certain problem**. If you can solve the problem without code, do that instead. Always try to keep this goal in mind.  If you can avoid writing some code by talking with someone and solving the same problem, then do that. Do less, but better.

## Code should be easy to change

What which of these two codebases do you prefer? One that doesn't work but you can change or the other which works but you can not change?

> Function or architecture? Which of these two provides the greater value? Is it more important for the software system to work, or is it more important for the software system to be easy to change?
>
> If you ask the business managers, they’ll often say that it’s more important for the software system to work. Developers, in turn, often go along with this attitude. But it’s the wrong attitude. I can prove that it is wrong with the simple logical tool of examining the extremes.
>
>   - If you give me a program that works perfectly but is impossible to change, then it won’t work when the requirements change, and I won’t be able to make it work. Therefore the program will become useless.
>   - If you give me a program that does not work but is easy to change, then I can make it work, and keep it working as requirements change. Therefore the program will remain continually useful.

## Good design is easy to change (pragmatic programmer)

The essence of good code design is that it is easy to change.

The world is full of people trying to sell you specific knowledge about how to write good software. There are lists, acronyms, patterns, diagrams, docks and many other things that try to tell you how to write good software. And then here I am as well. I am trying to tell you exactly how to write software. 

But there is a silver bullet. There is *one*.

And that one silver bullet is this: **Good design is easier to change than that design.**

All patterns, all techniques, all tooling that help you write good code like the hexagonal architecture, decoupling, and the single responsibility principle. All these things are special cases of this rule that they make your code easier to change. 

Why is decoupling good? Decoupling is good because when you isolate concerns you make things easier to change.

Why is the SRP good? The SRP is good because a change in requirements is then reflected in only one module.

Why is good naming important? Good naming is important because to change code you need to read it. 

Why is the hexagonal architecture good? Because when you want to change the technical infrastructure, it should be decoupled from the actual problem that you're solving. Making the code easy to change.

This is the main principle underlying all other principles: good code should be easy to change.

# Complexity (A Philosophy of Software Design)

## Introduction

The study of software is a study in complexity. We are taking information from some place, doing something with it, and putting it somewhere else. Fundamentally this feel and sounds very simple, but we all know what a mess we can make for ourselves. 

This piece talks about complexity, what is it, how can we reduce it, and why does it seem to always creep up on us without us noticing?

## Essential and accidental complexity

The study of software is basically a study of complexity.

What is complexity? How can we see if a system is complex? Why is working on complex systems hard? Are there ways for us to reduce it? 

There are two types of complexity: **essential** and **accidental** complexity.

* **Essential complexity**: Is the necessary complexity needed to perform a certain task. This complexity, at some level, is fundamental. If you want to do anything of significance you must have a certain minimum set of operations that do whatever you want to do. 
* **Accidental complexity**: This is basically all the complexity that you add while trying to achieve the essential complexity. This is everything that is not essential. The trick is to eliminate and minimize this type of complexity.

## Two ways of dealing with complexity

There are two ways you can deal with complexity, both the essential and the accidental type. 

* **Eliminate complexity**: The first way of dealing with complexity is to eliminate it. This is obviously good if it is possible. But often it is not that straightforward. 
* **Encapsulate complexity**: The second way of dealing with complexity is to encapsulate it. That is, can we hide the complexity of a certain module in the implementation such that when we are not working with it, we are not exposed to this piece of the complexity of the puzzle?

This is also the goal of **modular design**. The goal of modular design is to be able to work on a certain system without being exposed to all the complexity of the system. This is achieved with encapsulating complexity. There still is a certain amount of complexity in the system, but it is conveniently hidden for you when you are working on the system. The pieces of complexity that you are exposed to are expoed to you through the interface, its complex implementation is hidden by the interface.

## What is complexity?

Can we define complexity?

The book defines complexity as **“Complexity is anything related to the structure of a software system that makes it hard to understand and modify the system”**

This definition of complexity mirrors the essence of good design from: "Software should be easy to change" and most of the other books I've found.

This means that a system can be large and sophisticated, but if it is easy to change and easy to work on then the system is not complex in our vocabulary.

Burn this definition in your head: complexity is everything that makes code harder to change. 

# Architecture

## What is architecture (clean architecture)

So when we hear architecture, we hear sounds and visions of power and mystery. We think of weighty decisions and deep technical prowess, right? But what actually is software architecture? What does it do and when do you do it? The architecture of a software system is to shape given to that system by those who build it. The form of the shape is in how the system is divided into components, how they are arranged, and in the way that they communicate with each other. So in a sense, architecture is the invisible glue holding all the pieces together. Now we must never forget that the purpose of this shape is to facilitate the development, deployment, operation and maintenance of the software inside of it. The primary purpose of the architecture is to support the whole life cycle of the system. Good architecture makes the system easy to understand, easy to change and develop, easy to maintain and easy to deploy. The ultimate goal is to minimize the lifetime cost of the system and to maximize programmer productivity.

## What is architecture (clean architecture in python)

Every production system, every package, every medical mechanical device, or every action actually is made of components and the connections between them. The purpose of these components is to use the outputs of the components as inputs into some other components in order to perform a certain set of actions. In this process, the architecture specifies which components are part of an implementation and how they are interconnected. 

## The Golden Rule (clean architectures in python)

![](/../assets/software/2024-05-02-11-42-51.png)

> The Golden Rule: talk inwards with simple structures, talk outwards through interfaces.

> Your elements should talk inwards, that is pass data to more abstract elements, using basic structures, that is entities and everything provided by the programming language you are using.

> Your elements should talk outwards using interfaces, that is using only the expected API of a component, without referring to a specific implementation. When an outer layer is created, elements living there will plug themselves into those interfaces and provide a practical implementation.





# Tooling

## General Principles

- Dependency injection
- Information hiding / leaking
- Cohesion and coupling
- Separating data from computations
- Domain modeling and lightweight domain objects
- Input and output validation
- Separating tech from problem solving
- Local first

## Local > Cloud

Having things locally makes everything fast. Having to interface with the cloud takes time. Try to do as much as you can on your laptop. Why? Because this leads to quick feedback cycles and quick feedback cycles are important for you to figure out whether what you did was right or not. 

Example: Instead of testing `s3` directly, spin up a copy of `moto` using `docker-compose` instead.

## Use makefiles to automat tedious commands

Copy pasting 5 lines every time by hand is terrible.

Running `make build` feels great and snappy.

Let the computer do the work. Automate the boring stuff.

## Keep your feedback loop short

Try to make your feedback loop as fast as possible. This means for example having lightweight objects and writing tests for those objects. This means for example disabling steps in the pipeline so that you can run the tests faster. I am debugging a Docker pipeline now and I do not want to wait for the docker build every time but I am not changing the code, so I just disable the step so I can get faster to where the point that I'm trying to fix things. Make your feedback loops short so you get quick and timely feedback.

# Tests

## Unit tests should be fast

Unit tests should be fast. Unit tests should run in the order of seconds, preferably even milliseconds. You should run your unit tests often and they should not be a pain to run. If you feel like your unit tests take too long to run then that is a symptom of a larger problem. Probably you are hitting some external system that you do not want to hit. 

## Put your unit tests close to your source code

Conventional wisdom says that you should have a `src` folder and a `tests` folder. I disagree. Put your source code in files like `src/foo.py` and put your tests in `src/foo_test.py`. This convention is borrowed from [golang]() and [rust](). I like this convention because it promotes test code to be a first-class citizen. Testing no longer becomes an afterthought but it will garner the same attention and care as your other source (production code). 

## Integration tests should test the whole flow of the program

Integration tests should be a complete test of your system how the user would use it. This is basically an external API call to your system. How would someone use the interface that you expose to them? I put these in `test/` because I feel like this gives the distinction that they are external. These tests are heavy and often slow, don't have many of them.