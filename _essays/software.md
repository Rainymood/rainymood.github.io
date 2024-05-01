---
title: "How to write good code (draft)"
published: true
toc: true
toc_sticky: true
---

Goal:

* When someone asks me "How do you write good code?" this is the blog post I want to link them to.

# What is good code

## Code is for humans. Code is sociotechnical.

The first thing we should agree on is that code is social. Growth is written by humans. And code will be read by humans. This is very important because this means that every rule I make here about code, it might not actually translate across cultures. Every culture is different. People in different cultures are different. You know so. There's not really A1 size fits all reply. But I think there are some overarching principles that we can apply which make most of the code better.


## Code is read more often than it is written.

So a funny thing happens when you've been working at the same company for some time. You make a project, you write some code, you're finished a project, and then a year later you actually have to revisit your old project and you're like, wait, who built this piece of crap? And then you look into git commit and it's actually you that wrote it, so. Here we end up on a very funny principle, which is that code is read more often than is written.

Another way of framing this is that the second use write code, the second it goes from your head through your keyboard into the code base, it is now in maintenance mode. So this means that you will have to start maintaining it. And then imagine you have a project that has a lifespan of maybe one or two. Years. And you know it takes a week to write the code, but then if you look at it from the complete project perspective of two years. Most of the time will be spent in maintenance mode, so that is why it's so important that you write code that is easy to maintain, that you write code that is. So code is read more often than it is written. The second you write code, it has to become. It has to be maintained. So good code in that sense. Should be maintainable. Good code should be maintainable.

## Programming is problem solving

Writing code is not the end goal. The code exists to serve some greater purpose, to solve a certain problem. Always try to keep the goal in mind. If you can avoid writing some code by talking with someone and solving the same problem, then do that instead. Less but better.

## The best code is no code

The best code is no code. If you can do something in less lines, do it. Less lines of code means less things to maintain which means you can spend more time per unit. This increases quality and creates better software.

Do not pride yourself into using *lines written* but instead think of it as *lines spent*. 
## Good code should be understandable.

So another thing is that good code should be maintainable. It should be changeable. So there's this story in Clean Architecture or Clean Code, whatever. And the story basically goes like this. Imagine you have two code bases. The first code base works perfectly, but it's very hard to change. Actually, it's impossible to change. But it works perfectly. The second one, the code actually doesn't work. It doesn't work at all, but it is possible to change the code. Now I ask you, which one do you prefer? The one that works but is unchangeable, or the one that actually completely unfunctional but is changeable? Now, of course there's a correct answer to this question, and that answer is that it's the one that's changeable. Why? Because the world around us keeps changing. So the second you write code it becomes outdated and you have to maintain it. So even though the code now is not correct because you can change it, you have the future option for it to be correct. However, the code that is right now, but it's impossible to change will be wrong because the underlying world will change. So the summary of this is that good codes should be changeable, it should be easy to understand and it should be changeable. It should be changeable. You should be able to make changes.

# How do we write good code

- Dependency injection
- Information hiding / leaking
- Cohesion and coupling
- Separating data from computations
- Domain modeling and lightweight domain objects
- Input and output validation
- Separating tech from problem solving
- Local first




## Local is good

Having things locally makes everything fast. Having to interface with the cloud takes time. Try to do as much as you can on your laptop. Why? Because this leads to quick feedback cycles and quick feedback cycles are important for you to figure out whether what you did was right or not. 

Example: Instead of testing `s3` directly, spin up a copy of `moto` using `docker-compose` instead.

# Tooling

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