---
title: "What is knowledge tracing?"
date: 2022-08-23
tags:
- blog
- jekyll
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2022-08-23-knowledge-tracing-1-what-problem-are-we-solving/thumbnail.png"
---

In this blog post I want to talk to you about the problem of knowledge tracing. What is knowledge tracing, why is it important, and how do we define it?

Knowledge tracing is one of the problems that we spend a lot of time on at my [work](https://us.snappet.org/) and I feel incredibly fortunate that I'm working on tech that is trying to solve this problem.

**What is knowledge tracing?** Knowledge tracing tries to answer the following question: *How do we model a student's knowledge as the student interacts with an online learning platform?* 

**Example of knowledge tracing (Duolingo).** When you create a new account on Duolingo and you choose the language that you want to learn (say Dutch), Duolingo first asks you to do a little quiz to establish your current level of proficiency in Dutch. Modeling how good you are in Dutch (*modeling student knowledge*) based on your answers to this quiz (*interactions with the platform*) is exactly what knowledge tracing is! 

**More and better learning.** But why would we even want to model student knowledge? We do this in hopes that we can have more and better learning. To unlock every student's full potential and to level the educational playing field. This is mostly done in two ways: using personalized learning paths and personalized exercise suggestions.

**Personalized learning.** Knowledge tracing allows us to personalize learning paths for every individual student. When you think about it it makes perfect sense. Each student is unique. Hence, every student has an optimal learning path that is unique to that particular student, and tech can help us to find this unique path.

**Exercise suggestions.** Another benefit of knowledge tracing is that we can use this model we have of the student's knowledge to suggest the best exercise for that particular student at that particular time. Best, in this case means the exercise that would give the largest increase in learning result for that student. If we give an exercise that is too hard, the pupil won't be able to solve it. If we give an exercise that is too easy, the pupil won't learn anything.

Finally we are ready to define knowledge tracing as a mathematical problem

**Definition Knowledge Tracing:** We use the definition found in [this](https://arxiv.org/pdf/2002.07033.pdf) paper: *Given the history of a student's learning interactions in the past, what is the probability that the student will answer the next exercise correctly?* More specifically: 

* Let $E_i$ denote the *exercise information*, which contains things like the type of exercise, skills related to the exercise, and other exercise-related metadata
* Let $R_i$ denote the *response information*, which contains student response $r_i$ to exercise $E_i$ which contains things like whether the answer was correct, how long it took to response, and other response-related metadata
* Finally, let $I_1, \dots I_n$ be the sequence of recorded student interactions with $I_i = (E_i, R_i)$

Then, our aim is to predict, given the *previous* history of student interactions and the *current* exercise information, the probability of the student answering the $k$th exercise correctly:

$$P(r_k = 1 | I_1, \dots I_{k-1}, E_k)$$

**A trivial example:** Imagine we have a simple knowledge tracing model with 1 student, 1 exercise, $E_i = E = 1$, and 3 recorded responses, $R = (1, 0, 1)$. Our sequence of interactions is then $I=(I_1, I_2, I_3)=((1, 1), (1, 0), (1, 1))$. What would your prediction be if I give you this sequence
$I=((1, 1), (1, 0), (?, 1))$, in other words what would be your prediction be of $r_3$ given the new exercise $E$ and the history of interactions $I_1, I_2$:

$$P(r_3 = 1 | I_1, I_2, E_3))$$

But now imagine that we don't have just 1 exercise and 3 student interactions but that we have **millions of students** and **billions of student interactions**. This is the problem that we get to solve and [Snappet](https://us.snappet.org/) and that's why I love working there!

<!-- TODO: Add to about page -->