---
title: "How to write commit messages that will save you a lot of time" 
date: 2020-08-14
categories:
  - blog
tags:
  - blog
  - git
header:
  teaser: "/assets/2020-07-10-good-commit-messages/git_commit_2x.png"
---

Writing good commit messages can save you a lot of time. In this blog post I
want to show you an example of that. At some point in the past I changed the
colours of the links on this blog from grey to blue, but where did I make
this change again? Commit messages to the rescue!

<img src="/assets/2020-07-10-good-commit-messages/img.png">

I was unable to recall where in the code I made the changes by browsing
through the files so I went over my commit history and... lo and behold.

<img src="/assets/2020-07-10-good-commit-messages/commit.png">

Thank you, past me, for writing these awesome commit messages! 

## How to write good commit messages 

Writing good commit messages is a tricky thing and there are a
[lot](https://chris.beams.io/posts/git-commit/) of
[different](https://www.freecodecamp.org/news/writing-good-commit-messages-a-practical-guide/)
opinion on [this](https://github.com/erlang/otp/wiki/writing-good-commit-message).

What I like to do is follow a rule that I picked up somewhere. Sadly, I can't
find the source for this but it has served me well. The rule is as follows. When you write a commit messages you think to yourself 

>*When applied, this commit will...*

Here it is applied in action: 

* When applied this commit will **makes links blue**
* When applied this commit will **add logos and splash image**
* When applied this commit will **add splash post, leetcode post, update tags**

## Conclusion

I never thought that my commit habits would save me this much time, but here we are. To summarize, to write good commit messages simply think to yourself: 

>*When applied, this commit will...*

Thank you for reading! 

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
  <label for="mce-EMAIL">Liked this article and want to hear more?</label>
  <input type="email" value="" name="EMAIL" class="email" id="mce-EMAIL" placeholder="email address" required>
    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
    <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_92fe86c389878585bc87837e8_50543deff9" tabindex="-1" value=""></div>
    <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button"></div>
    </div>
</form>
</div>
<!--End mc_embed_signup-->