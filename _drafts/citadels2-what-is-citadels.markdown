---
layout: post
title:  "Citadels part 2 - What is Citadels?"
date:   2016-06-16 17:00:00 +0002
categories: jekyll update
---

# tl;dr

Citadels is a card game. I'm working on a clone of Citadels in Python. In this
blog post I talk how about what Citadels is, what a turn in Citadels looks like,
and my plan of attack for this little project. 

# What is Citadels

Citadels is a standard 'expand your empire by building buildings' card game, but
with a twist. You can expand your empire by building buildings from your hand by
paying the required amount of gold that is indicated on the card. But besides
that, before the round starts everyone chooses a role to play from a deck of
character cards ranked 1 to 8 (in the original set of cards).  Each character
has unique abilities that have a
sizeable effect on the gameplay. These character roles add a substantial layer of
depth to the game which is really fun and enables bluffing, scheming, etc. 

After everyone has picked a character card, the person with the 'wooden king
marker' (i.e. the person who took the King card last round) starts by calling
out each character by rank. The player with the King card summons a character as
follows: "I summon the assassin." and then the player with the assassin card
(rank 1) reveals his character card to be the assassin and starts his turn. If
no player has picked that character card then the King simply moves on to the
next character. The player who picked the King card that round receives the
wooden king marker. In the next round, he is the first to pick a character card
and he will call out each role to step forward. 

Now that I've vaguely talked about what Citadels is, what does a single turn in
Citadels look like?

# A turn in Citadels 

Let's set up the board first. We have 4 players, a deck of 8 characters, a deck
of 63 district cards, and a stash of golden coins. Everyone starts the game with
2 coins and 4 district cards. 

The 8 characters are as follows (with rank 1 through 8 respectively): assassin
(1), thief, magician, king, bishop, merchant, architect, warlord (8)

Each turn has the following phases

- Phase 1: Removing of characters
- Phase 2: Choosing of characters
- Phase 3: Player turns

## Phase 1: Removing of characters 

Before players are allowed to choose from the character deck, a single card is
removed from the character deck face down on the table. This leaves 7 character
cards to pick from. Then, depending on the amount of players, 0-2 randomly drawn
character are revealed on the table. Players can not choose from these revealed
characters. In a 4 player game 2 cards are revealed like this. This step leaves
5 character cards in the deck to choose from. 

## Phase 2: Choosing of characters

Now that some characters been removed from the deck, the choosing of characters
beings. The person with the king marker has the first pick. There is always a
person with the king marker because in the very first round the oldest person
receives the king marker. After the king has picked a character the person next
to him picks a character, etc. After everyone has picked a character, the
remaining 1 character card is put face down somewhere on the table as well. 

Each of the 4 players now have taken on a character role. 

## Phase 3: Player turns 

A player's turn begins when he (his character) is called out by the King. Assume
the player in this turn is the assassin. If the King calls out "I summon the
assassin to step forward." You reveal your character card and start your turn. 

Each character has a certain power which the player can use at _any_ time in his
turn. The assassin can 'murder' someone (the character, not the player!) who
then has to skip a whole turn. 

Let's say the assassin murders the thief by proclaiming: "I use my character
power and murder the thief!" When the thief is then summoned, he must remain
silent, although it is almost always glarinly obvious who got murdered.

Before building any buildings from you hand. You must do either one of the
following: draw 2 cards and put 1 back on the top of the deck, or take 2 gold
as income. Say the assassin takes the gold. He now has 4 gold in his hand
(because everyone starts with 2 gold) and can build cards from his hand. The
amount of gold a building (district) costs is indicated in the top left:

<!-- image of random district card -->
![King](/assets/citadels/prison-and-palace.jpg){:class="img-responsive" width="400px"}

The Prison costs 2 gold to build and the Palace costs 5 gold to build. As a general rule of thumb,
you should always try to build something as you are limited to building one
district each turn (unless you're the Architect character, he may build 3
districts each turn). Let's say the assassin builds the Prison (heh). To do so he
pays 2 gold to the bank and takes the card from his hand and puts it on the
table face up. He now has one red building: the prison. 

After a person is done with his turn, the King calls out the next character
cycle continues until every character has been called out. When everyone has
been called out, the character cards are collected and a new round starts with
phase 1. 

# Plan of attack

I really want to try to adhere to the KISS (Keep It Simple Stupid) principle. I
want to avoid unnecessary complexity as much as possible. 

Cards are represented by the `Card()` object, with a name, description,
cost, points, etc. I then make a global sort of card database named `CARDS`
which is a dictionary with all cards in it by name. `CARDS["Tavern"]` revers to
the card object for the tavern card. 

Players are represented by the `Player()` object with a `player.name,`,
`player.cards_in_hand`, `player.coins`, etc. 

The deck is simply a list of strings `deck = ["Tavern", "Dragon Gate", ... ]`
such that I can refer to the cards `CARDS[deck[i]]`. 

