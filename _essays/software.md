---
title: "How to write software"
published:
  false
---

# Mindset

## Programming is problem solving

Writing code is not the end goal. The code exists to serve some greater purpose, to solve a certain problem. Always try to keep the goal in mind. If you can avoid writing some code by talking with someone and solving the same problem, then do that instead. Less but better.

## The best code is no code

The best code is no code. If you can do something in less lines, do it. Less lines of code means less things to maintain which means you can spend more time per unit. This increases quality and creates better software.

Do not pride yourself into using *lines written* but instead think of it as *lines spent*. 


Test

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