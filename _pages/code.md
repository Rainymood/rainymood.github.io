---
permalink: /code/
title: "Architecture Patterns in Python"
toc: true 
---

The question we should ask ourselves is *not*: How do we write code that is functional, flexible, and easy to maintain?

The question we *should* ask ourselves is the following: How do we set up the code architecture in such a way that it only natural to write code that is functional, flexible, and easy to maintain?

The answer to this is a so-called **clean architecture** (or hexagonal architecture or onion architecture) and this page is dedicated to this concept.

On this page you will find a collection of concepts, blog posts, and visualisations so that you can apply the concepts and principles in your own work.

<img src="/assets/pages/code/hexagon.png" style="max-height: 500px">{: .align-center}


### Concepts behind a clean architecture

*TODO* 

### Components of a clean architecture

![](/assets/code/2023-02-26-15-54-02.png)

Let's take a look at the individual components that make up a clean architecture. 

The main four layers of a clean architecture are: 
* Entities: Entities contain a "representation of our domain model", it basically contains the building blocks of our application. These are kind of analogous to your data models, but they can be a bit richer than that. 
* Use cases: Use cases are processes that happen inside the application, this is where we apply our domain models to work on real data. These use cases are the whole reason why our application exists.
* Gateways: Gateways (sometimes called Ports I guess?) are the ways that our system interacts with the external systems. 
* External system: These are the external systems that our system interacts with. 

### Further reading

* One powerful principle is that of **inversion of control**, see this post: [Inversion of Control visualized]({% post_url 2023-02-04-inversion-of-control-visualized %})
* You have to **fight for flexibility** of the system, see this post: [A Tale of Two Values]({% post_url 2023-02-24-a-tale-of-two-values %})







Inspired by: 
* [Architecture Patterns in Python](https://www.cosmicpython.com/)
* [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

