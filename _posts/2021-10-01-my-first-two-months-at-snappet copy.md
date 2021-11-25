---
title: "DRAFT - My first two months at Snappet"
date: 2021-10-02
categories:
  - blog
toc: false
toc_sticky: false
tags:
  - update
header:
  teaser: ""
---

My first two months at Snappet have been great!

The project that I picked up is called *Big Calibration*. Big calibration is the process of taking all of the pupils answers and all of the questions in the Snappet platform and doing a single big recalculation of one of the core features of our model in production. The problem with Big Calibration was that it was broken, and I was tasked to fix it (actually, still am). 

Of course, without some context this sounds like plain gibberish. So first let me explain what Snappet is and then what Big Calibration actually is. 

## What is snappet?

![](/../assets/2021-10-01-my-first-two-months-at-snappet/2021-10-04-21-42-31.png)

Snappet is an online educational learning platform for primary schools. What this means is that we have created software that teachers can use in primary school to teach math and language. In schools that use Snappet, pupils make math and language exercises on tablets. We provide the tablets, educational platform, and teacher trainings. The teachers teach the Snappet method through the tablets, voila! 

![](/../assets/2021-10-01-my-first-two-months-at-snappet/2021-10-04-22-02-08.png)

The sort of vague hand-wavy explanation of how Snappet works internally is that every student has a thing called an "ability score". Every exercise has a thing called the "difficulty score". We try to give students the right level of difficulty by matching the students with the right ability to exercises with the right difficulties, and we use some sophisticated machine learning to do so. 

## Big calibration

![](/../assets/2021-10-01-my-first-two-months-at-snappet/2021-10-04-21-55-48.png)

Knowing that, Big Calibration is the process of taking **all answers from all students** from the start of the existence of the platform and **recalculating the ability and difficulty scores of the whole platform**. This might sound easy but let me tell you, we have more than 1.3 million (!) unique exercises, more than 3.2 unique users (with a big asterisk) and more than 3.8 billion (!!) answers in total. 

![](/../assets/2021-10-01-my-first-two-months-at-snappet/2021-10-04-22-05-38.png)

So we take all answers of all students and all exercises and their difficulties and we just put them in Big Calibration. Poof! Except, the problem was, it didn't work. Big Calibration stopped working for The Netherlands because of the sheer amount of data that we have collected. We have so many answers and so many students that our tensorflow just kept crashing. 

Of course, I just started working here and well. You know what might seem like a nice challenge. Yeah fixing Big Calibration. I have to admit I kind of took this on myself as well because I was really hungry for a technical challenge. Something to sink my teeth in. 

From a career perspective I'm not sure whether it was a smart move to start with such a hard and deeply technical project as my first. I still don't feel like I have a real good overview of the whole platform, so that's what I want to focus on for the next couple of months.

I've been writing a ton of python code, unit tests, integration tests, SQL scripts, the whole shebang. I think I rewrote around 80% of the original big calibration code base, using the starting code as a springboard. Rewriting legacy code is scary because you're not really sure where you are going, there were no real working tests to jump off from so I started with this semi-blank slate. What really helped me was the guidance of a senior engineer that kept my confidence high every step along the way. Sometimes I felt unsure what to do he came through and imbued me with new confidence to keep on pushing forward. 

## What tech have I been working with?

Most of my time is spent writing Python code or SQL really, which is nice. I feel like I've become much better at SQL after having to actually use it. I'm super amazed at the flexibility of "plain SQL". I'm amazed that such a big platform with billions of answers is handled by "just" some SQL tables. 

Our models in production run in Dockers on Sagemakers which I'm familiar with. I wasn't too familiar with Sagemaker but the API is well documented. For our code pipelines and CI/CD we use Azure DevOps which I had no experience with but it is straightforward enough. I don't feel confident enough to setup those pipelines from scratch but I've fixed and debugged some of the cloudformation templates as I had to. 

<!-- ## What is the remote/work from home situation at Snappet?

The situation is quite unclear really. We first got communication from leadership that we had to go to office once a week as a team but now suddenly we don't have to anymore. I personally like to go to the office because I like having a work place and a home place. I focus at work and relax at home. I have some people in my team that prefer to be completely remote. 

## Reorganisation

I joined Snappet right in the middle of a reogranisation, which is always a super interesting time of course to join. I joined Team Capybara's which was a real tight knit team which was really cool to see. THere was so much love and a real team spirit of caring for each other. However, their team reached the max capacity of like 14 people. The problem is/was that they were doing literally everything. Thecapybara team was resposndible for both the engineering part and the data science part of the machine learning models that were running inproduction.

This was way too much and the team was stretched too thin between concepting and building new things and maintaining old things. This is why the leadership decided to go for a reogrnasation and instead of having a data team now they split the data team up into an engineering team that is responsible for maintaing and keeping everything up and running, and the data science team is now more responsible for concepting new things from research and building the initial prototypes. 

Honestly we still have to see how this goes and this is comletely new for almost everyone here as well so I am super excited to be part o this and seeing where we end up. Tha being said when I joined (The last two mots) I really noticed that I was doin a lot of engineering work and not really a lot of data sicnece owrk. Id on't mind but yeah. 

## Am I having fun?

Fuck yes I am! Part of the reason that I left my previous employer was because I really felt like I had no mission, no purpose. And I wanted to join a purpose driven company. I have to say the people here they are really driven by the motivation to help the children as much as possible and for some reason that is just something so special. We all care about the children and we want them to succeed in our platform. All people that work here have this shared passion of helping children to make the best versions of themselves and I think that is honestly awesome!

## What am I looking forward to

I'm looking forward to writing more code, writing more tests, writing code that I am happy about that I wrote in 6 months. I am looking forward to finishing this project handing it off to engineering. I am looking forward to reading papers and doing more high level work getting an overview of the company. I am looking forward to working 2 days a week from home and 3 days in the office. My whole team works part time on friday which is super funn! 

## Becoming a better programmer with flashcards

I've also been using flashcards to remember programming Syntax and I really like it so far! For example how do we do this. Pop list first item. But then for everything. I make it a daily habit to check Anki.

## Brazilian Jiu Jitsu (BJJ)

I've also been training BJJ regularly for 3 days a week if my body keeps up on this. It's really nice that I've finally found a sport that I enjoy doing. I had a gym membership but going to the gym is boring. Jiu jitsu is fun *and* you get a workout while you're doing it. 

The whole premise behind jiu jitsu is to choke or submit other people through blood chokes or joint locks.

It's fun and really active and you really can spar against someone with your full power unlike boxing. Sparring is fun and it is important to test out your techniques against an opponent that is resisting.

"In theory there is no difference between theory and practice. In practice it is." 

I see so many parallels with life and life lessons you can get from jiu jitsu. I don't want to get too spiritual and high level here but there is this idea of like taking someone's force and redirecting it. If you are trying to get a sweep on somebody (throw him over) and he is resisting really hard the other way. Then why don't you just flip him the other way? That's the jiu jitsu way (how cringey it may sound). 

Another example, you always need to work both angles. If you know a sweep that pushes someone forward but he pressures backwards, then you wanna know a sweep that works backwards. You must keep your opponent guessing what you are going to do. 

What I also like about jiu jitsu is taht technique really shines. I've sparred against black belts there were a head shorte rthan me and they put me in a choke in like 30 seconds flat. It's amazing. That being said, jiu jitsu also teaches you that physical differences are *real* and that you should not underestimate how muc htechnique you can absorb using raw strength. Being on bottom and having someon that is 15 kgs heavier than you mount you... you'll notice. So this makes you so much more aware of your body.

All in all jiu jitsu is a great sport for me right now, it is really active, I get to fight 3 times a week, and it's fun! It's also social! everything I'm looking for ina a sport really. It is also super nerdy there are so many nerds here it surprises me.

## A checklist for work

This shouldn't really be here but I wanted to post this somewhere. So go over this checklist before you start working on a ticket. This way you don't miss anything stupid and you can start working on it:

Checklist before starting to work on a ticket:

- What is the output of this ticket?
- What is the problem? What do I need to solve? Can I write this down?
- Why is this a problem?
- What is the context of this?
- Can I break this ticket down into milestones/tasks?
- Can I work on this ticket independently? Do I need other people?
- Remind yourself that working independently does not mean working *alone*
- Remind yourself: dirty, validate, optimise -->

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
  <label for="mce-EMAIL">Liked this article and want to hear more? Join 40+ others and subscribe!</label>
  <input type="email" value="" name="EMAIL" class="email" id="mce-EMAIL" placeholder="email address" required>
    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
    <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_92fe86c389878585bc87837e8_50543deff9" tabindex="-1" value=""></div>
    <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button"></div>
    </div>
</form>
</div>
<!--End mc_embed_signup-->
