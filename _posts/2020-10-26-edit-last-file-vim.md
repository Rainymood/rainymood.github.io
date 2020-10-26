---
title: "How to open last edited file in Vim"
date: 2020-10-26
categories:
  - blog
tags:
  - blog
  - vim
header:
  teaser: "/../assets/2020-09-16-edit-last-file-vim/example-fg.gif"
---

While googling "How to open my last edited file in Vim", I found
[this](https://vi.stackexchange.com/questions/4817/is-there-a-vim-command-line-option-to-edit-last-edited-file)
excellent StackOverflow post.

![](/../assets/2020-09-16-edit-last-file-vim/2020-09-16-17-52-04.png)

It turns out that, in most Unix shells, you can suspend your current running process (Vim
in this case!) using `ctrl + z`, putting in the background.

Then to recover the Vim session you can use `fg` , which is a unix command
that continues a stopped job by running it in the foreground (fg) again. 

Here it is in action!

* `vim random.txt` to start the vim session 
* `Ctrl + Z` to suspend the vim session
* `$ fg` to bring it back up 

![](/../assets/2020-09-16-edit-last-file-vim/example-fg.gif)

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
  <label for="mce-EMAIL">Liked this article and want to hear more? Join 53 others and subscribe!</label>
  <input type="email" value="" name="EMAIL" class="email" id="mce-EMAIL" placeholder="email address" required>
    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
    <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_92fe86c389878585bc87837e8_50543deff9" tabindex="-1" value=""></div>
    <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button"></div>
    </div>
</form>
</div>
<!--End mc_embed_signup-->