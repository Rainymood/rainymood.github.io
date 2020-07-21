---
title: "What to do when your github credentials randomly start failing" 
date: 2020-07-21
categories:
  - blog
tags:
  - blog
  - git
  - tutorial
header:
  teaser: "/assets/2020-07-21-github-invalid/teaser3.jpg" 
---

You're coding. You're in the flow. You're banging code out at the speed of
light. You're building the software that is going to change the world. You
`git add` and `git commit`. You're on fire. You're unstoppable. You're
hackerman. 

<img src="/assets/2020-07-21-github-invalid/hacker.gif">

Then you try to `git push`

```bash
 ➜  git push
Username for 'https://github.com': Rainymood
Password for 'https://Rainymood@github.com':
remote: Invalid username or password.
fatal: Authentication failed for 'https://github.com/Rainymood/foobar.git/'
```

<img src="/assets/2020-07-21-github-invalid/no.gif">

What the hell?

# Everyone, PANIC! 

What the hell just happened? 

Honestly, I have no idea what just happened and why it happened. All I know
is that I've had this problem before and that my credentials sometimes
randomly just start failing when they feel like it.

Now you have to gather the last remaining pieces of self-worth you can find
around you on the floor and bash your head against a wall again to figure out
what the fuck went wrong and how to fix it.

# Step 1: Your username

First, we have to figure out what your user name is.

Let's consult `git config` to figure out your user name.

```bash
 ➜  git config user.name
Jan Meppe
```

WRONG! 

This is **not** your username. *This* is your user name. 

<img src="/assets/2020-07-21-github-invalid/img.png">

# Step 2: Your password

Second, we need to figure out your password. 

If you are not a savage and use a password manager you can find your password
for Github there.

<img src="/assets/2020-07-21-github-invalid/img2.png">

WRONG! AGAIN! 

This is **not** your password. If at some point in the past, you used this
thing called a *personal access token*, then *that token* is your password.
But you probably forgot about that, didn't you? (I for sure fucking did.)

Go to **Settings > Developer settings > Personal access tokens**

<img src="/assets/2020-07-21-github-invalid/img4.png">

Basically if you use any scripts that have this token hardcoded somewhere in
there will be absolutely fucked. Thankfully, I'm not such an idiot (I hope).

Regenerate the token for this particular device. 

<img src="/assets/2020-07-21-github-invalid/img5.png">

And now **this is your password**

<img src="/assets/2020-07-21-github-invalid/img6.png">

# Moment of truth 

We have our correct user name and correct password (personal access token).
Let's try this shit again.

```
 ➜  git push
Username for 'https://github.com': Rainymood
Password for 'https://Rainymood@github.com':
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 4 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 2.31 KiB | 2.31 MiB/s, done.
Total 6 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
```

YEEEEEES!!! IT WORKS!

This is what it feels to be in a love-hate relationship with an inanimate
thing. Stupid fucking git I hate you. At the same time you work seamlessly
100% of the time 60% of the time.

Stupid silly git.

# Still getting bothered? 

If you typed in your new password (personal access token) somewhere and it
worke you might still run into the issue of having to do it *again*. Of
course, no sane programmer wants to input his password every time he pushes
something.

To fix this, follow the instructions [here](https://docs.github.com/en/github/using-git/caching-your-github-credentials-in-git) and [here](https://docs.github.com/en/github/using-git/updating-credentials-from-the-osx-keychain) and [here](https://gist.github.com/nepsilon/0fd0c779f76d7172f12477ba9d71bb66).

What worked for me:

```
git config --global credential.helper osxkeychain
```

```
 ➜  git credential-osxkeychain erase
host=github.com
protocol=https
> [press return]
```

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
  <label for="mce-EMAIL">Liked this article and want to hear more?</label>
  <input type="email" value="" name="EMAIL" class="email" id="mce-EMAIL" placeholder="email address" required>
    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
    <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_92fe86c389878585bc87837e8_50543deff9" tabindex="-1" value=""></div>
    <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button"></div>
    </div>
</form>
</div>
<!--End mc_embed_signup-->