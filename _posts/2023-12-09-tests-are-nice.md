---
title: "Test-Driven Development win: Lessons learned using golang in Advent of Code"
date: 2023-12-09
tags:
- golang
- advent of code
- work
- engineering
- programming
- code
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2023-12-09-tests-are-nice/thumbnail.png"
---
<!-- ctrl + alt + v -->

Because the logic in part 1 of [Advent of Code Day 9](https://adventofcode.com/2023/day/9) did not seem so daunting, I wanted to challenge myself to really use Test-Driven Development. In this blog post I want to share some funny realizations that I had while doing so.

### Realization 1

**I made a lot of mistakes even for small and simple functions!** The first thing that I realized was that, even for small and simple functions, I was messing up big time. I was forgetting edge cases and making tiny mistakes all over the place. We really are bad computers. Even for this simple function that calculates the difference between the elements (`diff()`) I still needed multiple tries to get all the unit tests to pass. 

This unit test shows one of the unit tests for this function:

{% raw %}
```go
func TestDiff(t *testing.T) {
	input := []int{0, 3, 6, 9, 12, 15}
	expected := []int{3, 3, 3, 3, 3}
	output, _ := diff(input)

	if !reflect.DeepEqual(expected, output) {
		t.Errorf("Got %d, expected %d", expected, output)
	}
}
```
{% endraw %}

### Realization 2

**Tests pin down your results.** The second thing that I realized was that when you have use cases that you have nailed down as tests, they become facts. Every time you run the tests now you run your tests against these tests as a regression test. For example, in AOC they give you some input and output of a small example, and by virtue of turning that into a test case you turn that into a permanent fixture in your code. You can keep testing your code and verifying that your solution still satisfies that one test case, and that's really great!

> You pull out your handy Oasis And Sand Instability Sensor and analyze your surroundings. The OASIS produces a report of many values and how they are changing over time (your puzzle input). Each line in the report contains the history of a single value. For example:
> 
> ```
> 0 3 6 9 12 15
> 1 3 6 10 15 21
> 10 13 16 21 30 45
> ```
> 
> ...
> 
> If you find the next value for each history in this example and add them together, you get 114.

This test case fixes that input-output pair for the toy example mentioned in the text.

{% raw %}
```go
func TestSolve1(t *testing.T) {
	input := [][]int{{0, 3, 6, 9, 12, 15},
		{1, 3, 6, 10, 15, 21},
		{10, 13, 16, 21, 30, 45}}
	expected := 114
	output, _ := solve(input, true)

	if !reflect.DeepEqual(expected, output) {
		t.Errorf("Got %v, expected %v", expected, output)
	}
}
```
{% endraw %}

### Realization 3

**Debugging was so much easier.** Because I did not start slinging out code like a cowboy but instead wrote tests, I really was working incrementally. I knew exactly what pieces of my program I could trust (because I had tests) and which pieces of the program I could not trust (no tests), and this really helped with debugging. 

### Wrapping up

Today's challenge was quite easy logic wise so I had the chance to experiment a bit. I am using Advent of Code to teach myself golang and so far it has been a lot of fun. Golang feels a bit like a very spartan python, although golang is static, it feels very snappy and dynamic.

Cheers, Jan

**Remember** Tests are nice because they fix/pin down your results and they *prove* that your code works like you think it does. 
{: .notice--success}

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
    