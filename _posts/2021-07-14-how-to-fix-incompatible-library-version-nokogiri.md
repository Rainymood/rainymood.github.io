---
title: "How to fix an incompatible library version of nokogiri 1.10.10 in minimal mistakes" 
date: 2021-07-14
categories:
  - blog
toc: false
toc_sticky: false
tags:
  - jekyll
  - blog
header:
  teaser: "assets/2021-07-14-how-to-fix-incompatible-library-version-nokogiri/teaser.png"
---

Imagine trying to run your blog with `bundle exec jekyll serve` or `rake build` and suddenly you are hit by this incompatible library error: 

```
Traceback (most recent call last):
/Users/janmeppe/.rvm/gems/ruby-2.6.3/gems/nokogiri-1.10.10/lib/nokogiri.rb:30:in
`require': cannot load such file -- nokogiri/2.6/nokogiri (LoadError)
```

When I first encountered this error I had no idea what was going on.  What
happened in my case was that I ignored the security updates from Github pages
too long.  They fixed some security issues and if you use Github pages a bot
makes automated pull requests.  Obviously I ignored these security updates for
too long and at some point - poof - things started breaking. 

Anyway, here's how you fix it.

# Problem

You have an incompatible library version for nokogiri 1.1.0 and are using github pages.

This is the error you run into:

```
Traceback (most recent call last):
/Users/janmeppe/.rvm/gems/ruby-2.6.3/gems/nokogiri-1.10.10/lib/nokogiri.rb:30:in
`require': cannot load such file -- nokogiri/2.6/nokogiri (LoadError)
```

# Solution

You should have gotten an automated pull request in your repo like this:

![](/../assets/2021-07-14-how-to-fix-incompatible-library-version-nokogiri/2021-07-14-11-44-09.png)

1. Merge in this automated pull request to bump the nokogiri version
2. Uninstall all gems with `gem uninstall -aIx`
3. Install a new bundler `gem install bundler`
4. Install your gems with `bundle install`

That should fix it!

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
