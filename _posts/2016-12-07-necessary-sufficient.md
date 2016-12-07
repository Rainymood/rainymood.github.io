---
layout: post
title:  "Understanding Necessary and Sufficient Conditions"
date:   2016-12-07 00:00:00 +0200
categories: jekyll update
---

# Introduction

*tl;dr I always had a lot of trouble remembering and separating necessary and
sufficient conditions. After reading this blog post, I hope you will never forget the
difference again.*

Wheel.

![Wheel](/assets/necessary-sufficient/wheel.jpg){:class="img-responsive" width="200px"}

Potato.

![Potato](/assets/necessary-sufficient/potato.gif){:class="img-responsive" width="200px"}

Test.

![Test](/assets/necessary-sufficient/test.jpeg){:class="img-responsive" width="200px"}

Wheel?

![Wheel](/assets/necessary-sufficient/wheel.jpg){:class="img-responsive" width="200px"}

Potato?

![Potato](/assets/necessary-sufficient/potato.gif){:class="img-responsive" width="200px"}

Test?

![Test](/assets/necessary-sufficient/test.jpeg){:class="img-responsive" width="200px"}

Wheel? Potato? Test?

The signs?! What do they mean?! 

**What could driving, potatoes, and test possibly have in common?**

Right now? Not so much. But lets find out! 

# Definitions

Avoiding boring formal definitions, this is how I remember if a statement is
necessary: 

*If P is necessary for Q, then NOT P implies NOT Q.*

Similarly for a sufficient condition: 

*If P is sufficient for Q, then P implies (guarantees) Q.*

I will now give three examples which, in my opinion, beautifully illustrate the
concepts of necessary and sufficient conditions. Before truly understanding the
difference I always thought that sufficiency was a 'stronger' version of
necessary but this is not the case at all! They are two different things! 

# Necessary but not sufficient

The following statement is necessary, but not sufficient: 

**Driving straight is a necessary condition for driving well.**

The statement is necessary because NOT driving straight implies NOT driving
well. 

It is not sufficient because driving straight does not GUARANTEE that you
are driving well. For example, you can still be speeding. 

# Sufficient but not necessary 

The following statement is sufficient, but not necessary: 

**Boiling potatoes in water is a sufficient condition for getting boiled potatoes.**

It is sufficient because (obviously) boiling potatoes in water GUARANTEES boiled
potatoes. 

However, the statement is not necessary because NOT boiling potatoes
in water DOES NOT imply NOT having boiled potatoes (you might want to read that
twice). For example, you can still nuke your potatoes in the microwave to boil
them. 

# Both necessary and sufficient

Finally, the following statement is BOTH necessary AND sufficient:

**Answering all questions correct is a necessary and sufficient condition for
getting 10.**

The statement is necessary because NOT answering all question correctly
results in NOT getting a 10. 

The statement is also sufficient because getting all questions correct
GUARANTEES getting a perfect 10. 

# First and second derivatives

With this newfound knowledge we can now tackle the problem of the first and
second order derivatives and whether they are necessary, sufficient, both,
or neither. 

First, I now claim that:

f'(x) = 0 is a necessary condition for a maximum.

Is this true? If this is true then we have to check whether NOT f'(x) =/= 0 implies
NOT having a maximum. We see that this is the case. If the first
derivative is not equal to zero, then we will never find a maximum. Hence
the statement is indeed necessary. 

However, it is not 
sufficient because having only the first derivative equal to zero does not
guarantee a maximum, as we can also have a minimum!

Second, I now claim that:

f'(x) = 0 together with f''(x) < 0 is necessary and sufficient for a maximum.

This statement is necessary because indeed if we do NOT have this then we will
NOT have a maximum. 

This statement is also sufficient because if these things
are the case, then we know that we have found the optimum (if it exists) of a
strictly concave function (think of a mountain parabola thingy). Theory now says
that must have found a maximum. In other words these conditions GUARANTEE that
we actually find a maximum. 

# Conclusion

Now you know what driving straight, boiling potatoes, and getting all answers
correct on a test have in common: They are three prime examples of necessary and
sufficient conditions:

Driving straight is N but not S.

Boiling potatoes in water is S but not N. 

Getting all questions correct is N and S. 

I hope I was able to clear up any confusion you had about necessary and
sufficient conditions. Personally, I found this way of explaining necessary and
sufficient conditions very illuminating and I hope you think so too. 



