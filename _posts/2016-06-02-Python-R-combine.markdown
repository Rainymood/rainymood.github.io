---
layout: post
title:  "Python + R = Simpler life"
date:   2016-06-02 16:00:00 +0200
categories: jekyll update
---

## R 

In this post I want to show how I use Python to make my life a little bit easier
sometimes. For my MSc thesis I am working in R and dealing with a large amount
of technical indicators which I calculate in R as follows 

    # Rate of change
    roc1  <- ROC(data_$closing_price, n=1)
    roc2  <- ROC(data_$closing_price, n=2)
    roc3  <- ROC(data_$closing_price, n=3)
    roc4  <- ROC(data_$closing_price, n=4)
    roc5  <- ROC(data_$closing_price, n=5)
    roc10 <- ROC(data_$closing_price, n=10)
    roc15 <- ROC(data_$closing_price, n=15)
    roc20 <- ROC(data_$closing_price, n=20)
    roc50 <- ROC(data_$closing_price, n=50)

    # Simple Moving Average % Change
    SMAchange5  <- (data_$closing_price - SMA(data_$closing_price,
    n=5))/SMA(data_$closing_price, n=5)*100
    SMAchange10 <- (data_$closing_price - SMA(data_$closing_price,
    n=10))/SMA(data_$closing_price, n=10)*100
    SMAchange20 <- (data_$closing_price - SMA(data_$closing_price,
    n=20))/SMA(data_$closing_price, n=20)*100
    SMAchange50 <- (data_$closing_price - SMA(data_$closing_price,
    n=50))/SMA(data_$closing_price, n=50)*100

    # Exponential Moving Average % Change
    EMAchange5  <- (data_$closing_price - EMA(data_$closing_price,
    n=5))/EMA(data_$closing_price, n=5)*100
    EMAchange10 <- (data_$closing_price - EMA(data_$closing_price,
    n=10))/EMA(data_$closing_price, n=10)*100
    EMAchange20 <- (data_$closing_price - EMA(data_$closing_price,
    n=20))/EMA(data_$closing_price, n=20)*100
    EMAchange50 <- (data_$closing_price - EMA(data_$closing_price,
    n=50))/EMA(data_$closing_price, n=50)*100

    # Relative Strength Index
    rsi5  <- RSI(data_$avg_price, n=5)
    rsi10 <- RSI(data_$avg_price, n=10)
    rsi20 <- RSI(data_$avg_price, n=20)

    # Chande Momentum Osillator
    CMO5  <-  CMO(data_$closing_price, n= 5)
    CMO10 <- CMO(data_$closing_price, n=10)
    CMO20 <- CMO(data_$closing_price, n=20)
    CMO50 <- CMO(data_$closing_price, n=50)

    # Aroon oscillator
    Aroon5  <- aroon(data_$closing_price, n=5 )[,3]
    Aroon10 <- aroon(data_$closing_price, n=10)[,3]
    Aroon20 <- aroon(data_$closing_price, n=20)[,3]
    Aroon50 <- aroon(data_$closing_price, n=50)[,3]

Previously I added these together like this 

    technicals.unscaled <- data.frame(
        rsi5, rsi10, rsi20,
        roc1, roc5, roc10, roc20, roc50,
        SMAchange5, SMAchange10, SMAchange20, SMAchange50,
        EMAchange5, EMAchange10, EMAchange20, EMAchange50
        )

I figured that if I add more and more
indicators I have to add more and more of them by hand. I
thought this was very cumbersome and I figured this would be a perfect to hone
my Python-fu.

My goal is to write a little script that accepts input pasted from R in a text
file (like the first snippet) and generates output like the second snippet. 

## Python

I first copied the whole first snippet

    Contents of indicators.txt

    # Rate of change
    roc1  <- ROC(data_$closing_price, n=1)
    roc2  <- ROC(data_$closing_price, n=2)
    ...
    Aroon20 <- aroon(data_$closing_price, n=20)[,3]
    Aroon50 <- aroon(data_$closing_price, n=50)[,3]

to a file called `indicators.txt`. Lets open this file in Python and
see what we can find

    with open('indicators.txt','r') as file:
        for line in file.readlines():
            print line

Running this results in 

    ...
    CMO20 <- CMO(data_$closing_price, n=20)
    CMO50 <- CMO(data_$closing_price, n=50)

    # Aroon oscillator
    Aroon5  <- aroon(data_$closing_price, n=5 )[,3]
    Aroon10 <- aroon(data_$closing_price, n=10)[,3]
    Aroon20 <- aroon(data_$closing_price, n=20)[,3]
    Aroon50 <- aroon(data_$closing_price, n=50)[,3]

Note that the lines we actually want are the lines that contain `<-` which is
the assignment operator in R. Looping over only those lines with 

    with open('indicators.txt','r') as file:
        for line in file.readlines():
            if '<-' in line:
                print line
            else:
                pass

results in 

    ...
    rsi20 <- RSI(data_$avg_price, n=20)
    CMO5  <-  CMO(data_$closing_price, n= 5)
    CMO10 <- CMO(data_$closing_price, n=10)
    CMO20 <- CMO(data_$closing_price, n=20)
    CMO50 <- CMO(data_$closing_price, n=50)
    Aroon5  <- aroon(data_$closing_price, n=5 )[,3]
    Aroon10 <- aroon(data_$closing_price, n=10)[,3]
    Aroon20 <- aroon(data_$closing_price, n=20)[,3]
    Aroon50 <- aroon(data_$closing_price, n=50)[,3]

if we now apply the standard `.split()` function to each line 

    ...
    [CMO20', '<-', 'CMO(data_$closing_price,', 'n=20)']
    ['CMO50', '<-', 'CMO(data_$closing_price,', 'n=50)']
    ['Aroon5', '<-', 'aroon(data_$closing_price,', 'n=5', ')[,3]']
    ['Aroon10', '<-', 'aroon(data_$closing_price,', 'n=10)[,3]']
    ['Aroon20', '<-', 'aroon(data_$closing_price,', 'n=20)[,3]']
    ['Aroon50', '<-', 'aroon(data_$closing_price,', 'n=50)[,3]']

we see that all we have to do is to grab the first word after applying the split
function.  Starting from an empty string, we keep appending (`+=`) the first
word of each line we find with a comma and an enter in between as follows

    s = ""
    with open('indicators.txt','r') as file:
        for line in file.readlines(): 
            if "<-" in line:
                s += line.split()[0] + "," + "\n"
            else:
                pass
    print s

This running this results in

    roc1,
    roc2,
    roc3,
    ...
    CMO50,
    Aroon5,
    Aroon10,
    Aroon20,
    Aroon50,\n
    
Which is _almost_ what we want. But, there is something wrong. Actually
there are 2 things still wrong. The last two characters (you can't actually see
the `\n` in the output) need to be trimmed off. Trimming these off and wrapping
this in parentheses and the correct syntax we arrive at our final piece of code

    s = "technicals.unscaled <- data.frame("

    with open('indicators.txt','r') as file:
        for line in file.readlines(): 
            if "<-" in line:
                s += line.split()[0] + "," + "\n"
            else:
                pass

    s = s[:-2]+")" # remove the last "," and "\n"
    print s

Running this gives the following output 

    technicals.unscaled <- data.frame(roc1,
    roc2,
    roc3,
    ...
    CMO20,
    CMO50,
    Aroon5,
    Aroon10,
    Aroon20,
    Aroon50)

which is exactly the output we want. This can be copy pasted directly back into
RStudio!

If you have any questions or spot any errors, do not hestitate to reach out! 


