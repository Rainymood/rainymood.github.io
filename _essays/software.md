---
title: "How to write good code (draft)"
published: true
toc: true
toc_sticky: true
---

In this essay I try to write down everything I know about **writing good code**.

When someone asks me "How do you write good code" this is the blog post I want to be able to link them to.

The first section talks about **what is good code**.

Here I show that:

* Code is social
* Code spends most of its time in maintenance mode
* Code needs to be easy to change

The second section talks about **software architecture**.

Here I talk about:

* Software architecture
* What makes a software architecture good? (Spoiler: it's about being easy to change)
* The Golden Rule of software architecture

The third section talks about **tactics**

Here I try to provide very practical and specific tactics you can immediately apply in your day-to-day.

# What is good code

![](/../assets/software/2024-05-02-11-45-02.png)

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