---
layout: post
title:  "Scraping all songs played on sublime.fm in the last 30 days with Python!"
date:   2016-07-24 20:04:00 +0200
categories: jekyll update
---

I don't listen to radio often, but when I do, it's on
[sublime.fm](http://sublime.fm/).  Sublime.fm describes itself as 'fresh jazzy
sounds' and it basically plays a lot of jazzy funky music which is great to
groove out to once in a while. About a week ago I asked my girlfriend what song
was playing and she told me to check the site which shows the song that is
playing. 

I suddenly found myself wanting more, and wanting to figure out a way to get to
know all the songs that were played in the past or maybe figure out a way to
keep an updated list on the songs they have played in the past.  I felt like
this was a perfect opportunity to hone my Python-fu and keep it sharp.

My first idea was to scrape the sublime.fm website itself. However, the website
only shows the current song that is playing. It turns out that there is a
website (www.playlist24.nl) that actually keeps track of all these songs and
arranges them into playlists on their website. 

So basically, to figure out what songs have been playing in the last 30 days I
just have to check out that website, instead of the sublime.fm website itself.
My plan of attack is as follows:

1. Make it work for a single day (ex. 15-07-2016)
2. Figure out a way to make it work for multiple days

Let's get started! Let's first import some modules. For the scraping I use
BeautifulSoup and for obvious reasons we need datetime and urllib2 (although the
requests library could also be used)

```python
from bs4 import BeautifulSoup
import datetime
import urllib2
from IPython.display import display # prettyprint inside Jupyter notebook
```
Step 1 says that we have to make it work for a single day, so let's hardcode the
date first and later on make it variable. I'm using urllib2 to read in the
contents and then use BS4 to make it a soup which we can process later on.

```python
url = "http://playlist24.nl/sublime-fm/15-07-2016.html"
content = urllib2.urlopen(url).read()
soup = BeautifulSoup(content)
```

Taking a quick peek in the source code of the webpage we find this

```html
<span class="title">
<a href="/titel/2662/corinne-bailey-rae/trouble-sleeping.html">Trouble Sleeping</a>
</span>
<br/>
<span class="artist">
<a href="/artiest/2639/corinne-bailey-rae.html">Corinne Bailey Rae</a>
</span>
```

Which means that all we have to do is simply grab the text between the span
class 'title' and the span class 'artist'. It turns out that I had some code
lying around which does exactly that. 


```python
# find list of all span elements containing the words and definitions
titlespan  = soup.find_all('span', {'class' : 'title'})
artistspan = soup.find_all('span', {'class' : 'artist'})

# Create lists of lines corresponding to the element texts 
titles = [span.get_text().encode('ascii','ignore').replace("\n","") for span in titlespan][1:]
artists = [span.get_text().encode('ascii','ignore').replace("\n","") for span in artistspan][1:]
```

This method of using `.encode('ascii','ignore')` is actually not that safe and
results in some trouble which I have not yet found the time to fix. For example
`Beyoncé` gets changed to `Beyonc`. But this is an issue for later. Let's first
get a working prototype up and realize that we have made this little mistake
here. Taking a look at what `titles` and `artists` now look like


```python
print titles[0:3]
print artists[0:3]
```

    ['Trouble Sleeping', 'Never Never Gonna Give You Up', "He Won't Go"]
    ['Corinne Bailey Rae', 'Barry White', 'Adele']


The reason the `[1:]` on both lines is because the first matches of the span
class were `titel` and `artiest` (the dutch words for title and artist). Adding `[1:]`
pops off the first element of a list in Python. 

Zipping these together to create
tuples we can **extend** them to our final songlist. Note the `extend` and not
`append`. If we'd `append([1,2,3], [4,5])` the result would be `[1,2,3,[4,5]]`.
What we really want is `[1,2,4,5]` obviously.


```python
songlist = [] 
songlist.extend(zip(artists, titles))
display(songlist[0:10])
```


    [('Corinne Bailey Rae', 'Trouble Sleeping'),
     ('Barry White', 'Never Never Gonna Give You Up'),
     ('Adele', "He Won't Go"),
     ('4 Hero', 'Star Chasers'),
     ('Shalamar', 'The Second Time Around'),
     ('Jason Mraz', 'Hello, You Beautiful Thing'),
     ('Sly And The Family Stone', 'Everyday People'),
     ('Anita Baker', 'Caught Up In The Rapture'),
     ('Lenny Kravitz', 'I Belong To You'),
     ('Chaka Khan', 'We Can Work It Out')]


That seems to work! Exciting! That basically wraps up Step 1, doesn't it? Now let's make this bad boy work for multiple days. To do so we need a list of dates like `["24-07-2016","23-07-2016", ... ]` etc.

I figured that because yesterday is completely over (i.e. all songs have been
played) we should work back from yesterday instead of today. After asking Google
what to do, I found that yesterday can be represented by the following datetime
object (if that is the correct terminology) as follows


```python
yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
```

We can now create a list of days starting at yesterday with the following list comprehension. Obviously, `numdays` can be set to any number, but it only makes sense if the page exists (i.e. playlist24.nl/sublime-fm/dd-mm-yyyy.html) so we can scrape it, but let's keep it small for now.


```python
numdays = 2
date_list = [yesterday - datetime.timedelta(days=x) for x in range(0, numdays)]
```

Note that `date_list` is not a list of dates but rather a list of some sort of datelike objects which do not have the right representation yet.


```python
display(date_list)
```


    [datetime.datetime(2016, 7, 23, 19, 45, 33, 29389),
     datetime.datetime(2016, 7, 22, 19, 45, 33, 29389)]


See? So let's make the date variable! Remember the URL that we souped the contents of?


```python
url = "http://playlist24.nl/sublime-fm/15-07-2016.html"
```

We can use use `strftime(...)` to turn the objects in `date_list` into the proper format (i.e. dd-mm-yyyy like the good Europeans we are). 


```python
date = date_list[0].strftime('%d-%m-%Y')
display(date)
```


    '23-07-2016'


Refactoring the `url` has now become trivial


```python
url = "http://playlist24.nl/sublime-fm/{}.html".format(date)
```

Putting it all together with some added print statements we get the following piece of code


```python
from bs4 import BeautifulSoup
import datetime
import urllib2

yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
numdays = 2
date_list = [yesterday - datetime.timedelta(days=x) for x in range(0, numdays)]
songlist = []

for date in date_list:
    date = date.strftime('%d-%m-%Y')

    print "Scraping {}".format(date)
    url = "http://playlist24.nl/sublime-fm/{}.html".format(date)
    print "Fetching content ..."
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content)

    # find list of all span elements containing the words and definitions
    print "Finding titles and artists ..."
    titlespan  = soup.find_all('span', {'class' : 'title'})
    artistspan = soup.find_all('span', {'class' : 'artist'})

    # Create lists of lines corresponding to the element texts 
    titles = [span.get_text().encode('ascii','ignore').replace("\n","") for span in titlespan][1:]
    artists = [span.get_text().encode('ascii','ignore').replace("\n","") for span in artistspan][1:]

    print "Appending to songlist ... " 
    songlist.extend(zip(artists, titles)) # different than append! 
```

Running this results in 

    Scraping 23-07-2016
    Fetching content ...
    Finding titles and artists ...
    Appending to songlist ... 
    Scraping 22-07-2016
    Fetching content ...
    Finding titles and artists ...
    Appending to songlist ... 


The songlist looks promising


```python
display(songlist[0:10])
```


    [('Michael Jackson', 'Gone Too Soon'),
     ('Fkj & Jordan Rakei', 'Learn To Fly'),
     ('Lyn Collins & James Brown', "It's Alright"),
     ('Rose Royce', 'Car Wash'),
     ('Sergio Mendes & John Legend', "Please Baby Don't"),
     ('Leela James', 'Fall For You'),
     ('Curtis Stigers', 'I Wonder Why'),
     ('Al Jarreau', "We're In This Love Together"),
     ('Jill Scott', 'Back Together'),
     ('Caro Emerald', 'Back It Up (New Mix)')]


But I know for a fact that they often play the same song so we also need to remove the duplicates from the songlist. `set()` takes care of that for us! Saving the original songlist with the duplicates we can figure out how many duplicates were removed.


```python
songlist_with_duplicates = songlist
songlist = list(set(songlist)) # remove EXACT duplicates
print "Removed {} duplicates".format(len(songlist_with_duplicates) - len(songlist))
```

    Removed 0 duplicates


All that's left is to save the output into a properly formatted `.txt` file and we're all set!


```python
outfile_name = "songlist-back-to-" + date_list[-1].strftime('%d-%m-%Y') + ".txt"
with open(outfile_name, 'w') as out:
    for combination in songlist:
        out.write(','.join( ("\"" + str(s) + "\"") for s in combination) + '\n')
print "Saving output in {}".format(outfile_name)
```

Results in 

    Saving output in songlist-back-to-22-07-2016.txt

We're done! The complete code piece is then as follows

```python
from bs4 import BeautifulSoup
import datetime
import urllib2

yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
numdays = 30
date_list = [yesterday - datetime.timedelta(days=x) for x in range(0, numdays)]
songlist = []

for date in date_list:
    date = date.strftime('%d-%m-%Y')

    print "Scraping {}".format(date)
    url = "http://playlist24.nl/sublime-fm/{}.html".format(date)
    print "Fetching content ..."
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content)

    # find list of all span elements containing the words and definitions
    print "Finding titles and artists ..."
    titlespan  = soup.find_all('span', {'class' : 'title'})
    artistspan = soup.find_all('span', {'class' : 'artist'})

    # Create lists of lines corresponding to the element texts 
    titles = [span.get_text().encode('ascii','ignore').replace("\n","") for span in titlespan][1:]
    artists = [span.get_text().encode('ascii','ignore').replace("\n","") for span in artistspan][1:]

    print "Appending to songlist ... " 
    songlist.extend(zip(artists, titles)) # different than append! 

print "Removing duplicates"
songlist_with_duplicates = songlist
songlist = list(set(songlist)) # remove EXACT duplicates
print "Removed {} duplicates".format(len(songlist_with_duplicates) - len(songlist))

outfile_name = "songlist-back-to-" + date_list[-1].strftime('%d-%m-%Y') + ".txt"
with open(outfile_name, 'w') as out:
    for combination in songlist:
        out.write(','.join( ("\"" + str(s) + "\"") for s in combination) + '\n') 
print "Saving output in {}".format(outfile_name)
```

Running the code with `numdays = 5` results in

```raw
Scraping 23-07-2016
Fetching content ...
Finding titles and artists ...
Appending to songlist ...
Scraping 22-07-2016
Fetching content ...
Finding titles and artists ...
Appending to songlist ...
Scraping 21-07-2016
Fetching content ...
Finding titles and artists ...
Appending to songlist ...
Scraping 20-07-2016
Fetching content ...
Finding titles and artists ...
Appending to songlist ...
Scraping 19-07-2016
Fetching content ...
Finding titles and artists ...
Appending to songlist ...
Removing duplicates
Removed 518 duplicates
Saving output in songlist-back-to-19-07-2016.txt
```

with `songlist-back-to-19-07-2016.txt` as follows 

```raw
"Dionne Bromfield Ft Lil Twist","Foolin"
"Sting","Fragile"
"Robert Palmer","Best Of Both Worlds"
"Jocelyn Brown","Somebody Else's Guy"
"Bob Sinclar & Gary Pine","Love Generation"
...
```

That's all for now! I totally agree with you that this is far from perfect but
it works! Hopefully you've enjoyed this small blog post and
maybe learned a thing or two. I hope I have made you guys a little bit more
excited to learn Python perhaps or to do these little side projects yourself.
I'm looking forward to them! Programming is automation, and it's awesome! 
