---
layout: post
title:  "Writing a cardgame (Citadels) part 1!"
date:   2016-05-26 14:00:00 +0200
categories: jekyll update
---

# Citadels

So a while ago I was playing this awesome cardgame called Citadels with my
dearest friends and I was like man this is really cool! I thought to myself: why
not create a program? This medium sized project is pretty cool, good in scope
(i.e. not too large) and I should be able to finish this.

Before writing any code, we have to go the drawing board and think of what kind
of classes and functions (etc.) we need. 

Citadels is an intricate turn-based cardgame based around building buildings and
creating an empire, but there's a twist. Before the building phase, each player
secretly takes on a role from the available character cards. Each character has
specific abilities that make the game a lot more interesting. 

The thief for example can steal from another character. The assassin can
"murder" another character such that that character has to skip a whole turn.
Usually players are restricted to only building one building, unless you're the
architect, then you can 3 buildings at max.  There (if we use the vanilla game)
8 different characters: assassin, thief, magician, king, magician, merchant,
architect, and warlord. 

Let us brainstorm about what the player class should have. 
