---
title: "Advent of Code 2024 in Rust"
date: 2025-01-02
tags:
- blog
- work
- rust
- advent of code
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2025-01-02-advent-of-code-2024-in-rust/thumbnail.png"
---
<!-- ctrl + alt + v -->

**tl;dr Did Advent of Code (AOC) 2024 in Rust and got 27 stars ⭐️**


![](/../assets/2025-01-02-advent-of-code-2024-in-rust/2025-01-02-22-44-23.png)

Last year I used Advent of Code (AOC) to try out Golang, this year I used AOC to learn rust.

The challenge where we had to find this christmas tree being made by a swarm of drones was pretty fun

![](/../assets/2025-01-02-advent-of-code-2024-in-rust/2025-01-02-22-46-58.png)


# The programming language is a detail

When you squint hard enough, the programming language you solve AOC with is an implementation detail.

I think it’s nice if you can solve the problem “in your head” (on paper) and then you only need to write the implementation in any programming language, hence, a detail.

With python I did not feel the need to solve it on paper first. With rust I do.

I noticed that for the AOC challenges done in python you can just hack away at your liking because the language is very flexible and iterative. 

For Rust and also Golang I’m noticing that I get a lot of value out of thinking of the whole flow first on paper, the data structures, and then programming it all in. I guess this is because the language is less flexible.

# Rust is fast

Rust is faaast.

One thing I noticed immediately in the first couple of days is that rust is really fast. The first day my runtime of part 1 and 2 was 0.8ms. On the second day I got a runtime of part 1 and 2 of 13ms. Coming from Python this is like having super speed unlocked, which is an awesome feeling.

# In Rust you “can not use the same variable twice”

Rust's ownership system is what makes it fast, but it also makes you think a bit about how memory is laid out. The learning curve is steep and I'm learning it now, or attempting to at least.

Here's a small example, coming from someone that works with Python.

One rule of the ownership system is that every variable has one owner and exactly one owner. When this owner goes out of scope the variable is dropped. 

A consequence of this is that you "can not use the same variable twice". For example:

```python
a=10 # a owns 10
b=foo(a) # b now owns 10, a no longer owns 10
```

Now you can not use `a` anymore because ownership was given to `b`. 

This ownership system is what makes Rust fast, but also what makes it difficult to work with.

I know I did a terrible job explaining the ownership system, but this makes it somewhat understandable from a Pythonista perspective, I think.

# I am using ChatGPT quite a bit and it’s great (so far)

I output a lot of code with ChatGPT.

I was always a bit skeptical but I have to admit it is a big help.

Yes, I am writing a lot of shitty code. No it might not be the best code. But it is code that works and if I can output 10x the code at half the quality, I guess it is still a win?

For me, the challenge or learning curve is producing **working** rust code, not writing the best rust code. 

For me, good now means working, whether I wrote it or ChatGPT wrote it. 

When you think about it we write tests that fix down some behaviour and then we write code to make the tests pass. But there are many versions of the code that make the tests pass, so why not have ChatGPT write some?

If I'm really honest sometimes ChatGPT thinks of more edge cases than I do. Computers don't make mistakes, humans do.

Honestly, ChatGPT is really great. Especially for fighting WITH the borrow checker. Inputting an Error gives me some explainer in normal people language that a noob like me can work with.

ChatGPT shouldn’t become a crutch that I should lean on too heavily. 

But at the same time people use Google as a crutch as well. It works, for me, now.

# I struggled with and learned how and when to use references

I struggled quite a lot in trying to understand when to use a borrow or a mutable borrow and in that struggle I think I gained some experience fighting the borrow checker. 

Before, I would just change my code until it worked, but then I found some information on the internet

![](/../assets/2025-01-02-advent-of-code-2024-in-rust/2025-01-02-22-44-49.png)

I learned that you want to follow the principle of LEAST permission. So the order goes something like this: first a borrow, then a mutable borrow, and then full variable ownership.

Or this one

![](/../assets/2025-01-02-advent-of-code-2024-in-rust/2025-01-02-22-44-59.png)

Talking with another colleague he explained it as follows: Try to write functions that return new types themselves and then just pass in borrowed values, then you don’t need to think about ownership all that much.

# In the beginning I leaned into ChatGPT really hard

I let ChatGPT write me a lot of rust code.

I’m not sure if this was a good move, but it produced working rust code. I realized it was/is a crutch that needs replacing at some point. But my whole point was not to write perfect rust code. The challenge for me was to **write working rust code** and that would solve the advent of code challenge. 

# Impressed by ChatGPT

I am quite impressed with the Rust code that ChatGPT writes.

It writes code that is literal to your spec and not elegant, but it is an AI trained on the collective minds of everyone that it was trained on. If you give good and atomic specifications, it does spit out working code, and that’s quite impressive to me.

I do have to admit that writing out the solution on paper helped a lot.

# Reflections after day 4

Having small test cases for the normal use cases and edge cases helps a lot.

Having a test for reading in the data really helps.

Write out the solution on paper before and think about the functions you need.

In essence what you are making is a function mapping `filename -> solution`

You have to read in, parse, solve, and return, and that’s it.

ChatGPT is writing crazy good code.

Tests help A LOT with reproducibility of the solution.

TESTS HELP A LOT. 

Can not be repeated often enough.

# ChatGPT actually makes mistakes

I experienced that for some very simple parsing questions, ChatGPT made a lot of annoying off-by-one errors. I sort of expected it? Maybe? But it was still  a bit annoying. An example:

```python
convert this

............
........0. .. <== three dots ". .."
.....0 .. .. ..
.......0....
....0 .. .. .. .
......A.....
............
............
........A...
.........A..
............
............

 to a vec<vec<char>>
```

Notice that the second line has 3 dots on the right.

However, the converted vector has four dots.

```python
let grid: Vec<Vec<char>> = vec![
    vec!['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    vec!['.', '.', '.', '.', '.', '.', '.', '0', '.', '.', '.', '.'], four dots
    vec!['.', '.', '.', '.', '.', '0', '.', '.', '.', '.', '.', '.'],
    vec!['.', '.', '.', '.', '.', '.', '.', '0', '.', '.', '.', '.'],
    vec!['.', '.', '.', '.', '0', '.', '.', '.', '.', '.', '.', '.'],
    vec!['.', '.', '.', '.', '.', '.', 'A', '.', '.', '.', '.', '.'],
    vec!['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    vec!['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    vec!['.', '.', '.', '.', '.', '.', '.', '.', 'A', '.', '.', '.'],
    vec!['.', '.', '.', '.', '.', '.', '.', '.', '.', 'A', '.', '.'],
    vec!['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    vec!['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
];
```

# Trick: You can represent a grid of numbers with a hashmap

This is a technique that I saw somewhere in someone’s Rust solution and that I will be stealing for sure. 

You can represent a grid like `grid[row][col]` with a hashmap instead. This allows you to do out of bounds checking by simply checking if the key does or does not exist. This blew my mind.

# Integer division fucked me up a couple of times

I learned painfully that integer division works like you’d expect from integer division (

```python
let num_a = p1 * d / denominator - p2 * b / denominator;
let num_b = p2 /denominator * a - p1 / denominator * c;
// let num_b = p2 /denominator * a - p1 / denominator * c;

```

![](/../assets/2025-01-02-advent-of-code-2024-in-rust/2025-01-02-22-45-17.png)

# Hashmap initialization

Learned how to do this initialization. There are probably nicer and better ways. But this is one of them I guess. Something I had to do quite often in AOC

![](/../assets/2025-01-02-advent-of-code-2024-in-rust/2025-01-02-22-45-30.png)

# Wrapping around grids can be annoying

There was one problem where I had to wrap around a grid which was a bit annoying. I solved this by taking the modulo in the end.

> To fix this problem, we add numRows to i before taking the modulo numRows. This ensures that we're always taking the modulo of a positive number. Now we can count the number of live cells among the eight neighbors of grid[row][col] as follows.


# What I would have done differently

In hindsight I should have and would have liked to invest more in “the basics”

Basics like how do vectors work, what is `.iter()`, how does `.collect()` work etc.

But honestly without a really good reason to do these they are less FUN than just solving these little puzzles and grinding your way through.

Solving these programming puzzles, with no matter how shitty code, is fun and engaging. 

It’s what keeps me learning.

So whatever you do, whatever crutch you need (I used ChatGPT), try to STAY ENGAGED! 

![](/../assets/2025-01-02-advent-of-code-2024-in-rust/2025-01-02-22-46-29.png)

# Invest in debugging tools

One thing that I can suggest is to invest in debugging tools.

Like if you have a grid, ask ChatGPT to write a function to print it out. 

Especially for the later puzzles, they are hard with many edge cases.

You will forget something and probably won’t get it correct on the first try.

To hedge this, invest in your debugging toolkit where you can print out the state and have it match with the exercise at hand. 


![](/../assets/2025-01-02-advent-of-code-2024-in-rust/2025-01-02-22-46-58.png)

# Mistakenly used binary XOR for to the power

I used `2^x` to try and to the power something, but this is the binary XOR operator. 

```yaml
let num = (A / 2^combo.get(&operand).expect(""));
```

This didn't work as expected. Oops.

# Thanks Reddit

I was stuck on some problem and then someone on Reddit gave this hint and I had exactly the same problem. I fixed the first division but there were 2 other instances I had to fix. Thanks Reddit.

> Part 1 is a nice simple bytecode interpreter, but with quite a few opportunities for bugs. I coded it slowly and carefully, but forgot to actually do the division in the division opcode, and when I fixed the bug I forgot there were two other division opcodes to fix.


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
<label for="mce-EMAIL">I blog about how to grow as a machine learning engineer! Liked this article and want to hear more? Join 40+ others and subscribe!</label>
<input type="email" value="" name="EMAIL" class="email" id="mce-EMAIL" placeholder="email address" required>
    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
    <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_92fe86c389878585bc87837e8_50543deff9" tabindex="-1" value=""></div>
    <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button"></div>
    </div>
</form>
</div>
<!--End mc_embed_signup-->
    