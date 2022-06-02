---
title: "Study notes on hash tables (EPI)"
date: 2022-06-01
tags:
- blog
- jekyll
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2022-06-01-study-notes-on-hash-tables-epi/thumbnail.png"
---

A hash table is a data structure used to store keys, optionally, with corresponding values. 

Inserts, deletes, and lookups are O(1) time on average. 


The underlying idea is to store keys in an array. 

A key is stored in the array locations, called "slots", based on its "hash code".

A hash code is an integer computed from the key by a hash function.

If the hash function is chosen well, the objects are distributed uniformly across the array.

If two keys map to the same location, a "hash collision" is said to occur. 

The standard mechanism of dealing with this is to maintain a linked list of objects at each array location. 

I still don't really understand this. How hash collisions are dealed with. We can rehash the array by moving it to a new location.

A hash table is qualitatively different from a sorted array:

1. Keys do not have to appear in order
2. Randomization (the hash function) plays a central role

Compared to binary search trees (which I don't understand yet), inserting and deleting in a hash table is more efficient. 

One disadvantage is that you need a good hash function, but this problem is solved.

A hash function has one hard requirement: equal keys should have equal hash codes. 

This may seem obvious but is easy to get wrong, for example, by writing a hash function based on the address instead of the contents, or by including profiling data.

Another softer requirement is that the hash function should "spread" keys uniformly in the array. And it is nice if it is efficient to compute.

A common mistake with hash tables is that a key that is present in the hash table will be updated.  The consequence is that the lookup for that key will now fail, but it is still in the hash table. If you want to update a key, remove it, update it, then add it back, this ensures it is moved to the right array location. I feel like this is more important for languages with memory and pointers etc. Not python.

## Application of hash tables in anagrams

Anagrams are popular word  play puzzles, where rearranging letters of one set of words you can get another set of words. For example, "eleven plus two" is an anagram for "twelve plus one". 
Crossworld puzzle enthusiasts and Scrabble players benefit from the ability to view all possible anagrams of a given set of letters.

Suppose  you were asked to write a program that takes as input a set of words and returns groups of anagrams for those words. Each group must contain at least two words.

For example if the input is "debitcard", "elvis", "silent", "badcredit", "lives", "freedom", "listen", "levis", "money" then there are three groups of anagrams: 1) debitcard and badcredit, 2) elvis, lives, levis, 3) silent, listen). Note that money is not an anagram.


Let's begin by considering the problem of testing whether oen word is an anagram of another. Anagrams do not depend on the ordering of characters so we can perform the test by sorting the characters of the string. A string is an anagram if they are equal after sorting `sort(elvis)` is the same as `sort(levis)`. 


The first step is to always come up with a brute-force solution that works but is slow and expensive. The most obvious way is just to loop through all the strings in the array. We start at the first one, sort it, and then go over all the other arrays, sort them, and look whether they match. If they match we don't consider the second string again. This leads to an O(n^2mlogm) algorithm where n is the number of strings and m is the max string length. 

This works, but is slow. I

The key idea  is to use the sorted string as the hash identifier. Given any string, its sorted version can be used as a unique identifier for the anagram group it belongs to.

What we want is a map from a sorted string to the anagrams it corresponds to. **Anytime you need to store a set of strings, a hash table is an excellent choice**. 

Our final algorithm proceeds by adding  `sorts()` for each string `s` in the dictionary to  a hash table. The stored strings are keys and the values are arrays of the coresponding strings from the original input. 

CODE

The computation consists of n calls to sort and n insertions into the hash table. Sorting keys has a time complexity of O(nmlog(m) ) the insertions are O(nm) yielding O(nm log m) time complexity in total.

Questions/flashcards:
* What is a hash code
* What is the standard way of dealing with hash collisions
* What is the one hard requirement for a hash function
* When is a word an anagram?
* Anagrams we can solve with?
* Palindromes we can solve it?
* What is the brute force method to solve anagram problem?
* What is the elegant method of solving anagram problem?
* When is a hash table an excellent choice?
* Sorting is O(...)
* Sorting n keys is O(...)