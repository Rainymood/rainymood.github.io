---
layout: post
title:  "Writing a cardgame in Python part 1 - cards"
date:   2016-06-16 17:18:00 
categories: jekyll update
---

# Preface

So I am working on porting a card game (Citadels) in Python. My plan is to first
write a command line interface (CLI) program and then extend this with a GUI and
perhaps even a web GUI. But let's keep it simple. 

I actually started with the `Player` object, but as of right now the project is
already quite far from the start. Because of this I thought it might be better
to simply write some stuff about what I am currently working on as that is still
fresh in the mind. 

Today, I talk about cards.

# The card class

To design the card class, I ask myself: what does a card _have_ and what does a
card _do_. For example, a `Dog` has a `Dog.fur_colour` and a dog barks, hence
`Dog.bark()`. This is an example of a district card in Citadels

<!-- image of random district card -->
![King](/assets/citadels/prison-and-palace.jpg){:class="img-responsive" width="400px"}

A card itself (next to it's effects on the game) doesn't really
_do_ anything, so we'll leave the functions empty for now. 
What does a card _have_? Well from the image above we see that each card has a
name, each card has a description, it has a colour (the colour of orb on the bottom left), (not pictured)
a card is worth some amount of points (if built), and some cards (the purple
ones) have special effects: 

<!-- image of purp card -->
![King](/assets/citadels/haunted-city.jpg){:width="200px"}

Perhaps this method of designing classes is completely wrong so please correct me
if I'm wrong. Well then, let's fire up a python file called `cards.py`. We now
have enough information to start writing the `Card` class:

```
class Card(object):
    def __init__(self, name, description, cost, points, color, amount):
    # effects are incorporated in the game logic 
        self.name = name
        self.description = description
        self.cost = cost
        self.points = points
        self.color = color
        self.amount = amount
```

I completely forgot to mention the last one `self.amount = amount`. Which is
kind of funny because I forgot that one as well, until had to add it. Each deck contains
a certain number of each card. A normal deck for example has I believe 5 Taverns
in it but only 1 Dragon Gate. This variable is used when constructing the deck,
which I'll get to later. 

I just said that a card 'doesn't really do anything', this is not true obviously
as there are some cards that have an effect on the game play. I made a conscious
choice here to incorporate these cards in the game logic, as I see no elegant way
to put the effects in the cards somehow. If you have a good suggestion please do
not hesitate to reach out to me! I'm wondering how much this decision will bite
me in the ass later on. 

My first choice was to model the cards as separate objects for each card like
this 

```
tavern = Card(name = "tavern",
              description = "A tavern.",
              cost = 1,
              points = 1,
              color = "green"
              )
```

I thought myself ... that is really stupid. I then turned to excel and
created a simple `.csv` file which was way quicker than creating each object by
hand. Here's a screenshot of the `.csv` file

<!-- csv cards -->
![King](/assets/citadels/csv.png){:class="img-responsive"}

Now I have to find a way to convert this file to card objects. Python to the
rescue! It turns out there is a really easy way to do this. But I did run into
some errors. The main bug that took me quite a while to figure out was this:
"new-line character seen in unquoted field - do you need to open the file in
universal-newline mode?" The fix I found for this was to not just open the
`.csv` as read (`r`) but as universal read (`rU`)

The `DictReader()` creates a dictionary for each row in the `.csv` file and uses
the first row of the file as the keys. This is exactly what we want. Originally
I wanted to use the same variable names for the objects (i.e. the variable
Tavern contains the object Tavern,
etc.) but this idea got quickly shut down by some Stack Overflow posts. They
practically all said that using dictionaries for this is way safer and more
manageable. 

So I first create an empty dictionary. Reading in row by row first a
`card_object` is created with the proper name, description, etc. Then this
object becomes the value in a dictionary with the name of the card as the key. 

```
CARDS = {}
with open('cards.csv', 'rU') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', dialect =csv.excel_tab)
    for row in reader:
        card_object = Card(name = row['name'],
                           description = row['description'],
                           cost = int(row['cost']),
                           points = int(row['points']),
                           color = row['color'],
                           amount = int(row['amount'])
                           )
        CARDS[row['name']] = card_object
```

After running the `cards.py` we can see that it actually works like we want to

```
In [3]: CARDS['Tavern']
Out[3]: <__main__.Card at 0x111184ad0>
```

So the actual value at the key is an object which we can access 

```
In [9]: CARDS['Tavern'].name
Out[9]: 'Tavern'

In [10]: CARDS['Tavern'].points
Out[10]: 1

In [11]: CARDS['Tavern'].cost
Out[11]: 1

In [12]: CARDS['Tavern'].color
Out[12]: 'green'
```

Oh another funny thing: I actually forgot to read in `points =
int(row['points'])` with the `int()` function around it so it defaulted to a
string value. This went unnoticed until  I started doing arithmetics with it. I
quickly sorted it out but you see how easy it is for these kind of bugs to creep
in! 

I feel like this post has become way too long already for one post so I'll cut
myself off here. In the next post I'll show you how to turn these cards into a
real deck! 

I hope you enjoyed this and if you have any questions or comments don't hesitate
to reach out to me through either the comment section or any other method!

\- Jan 
