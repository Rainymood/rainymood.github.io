---
title: "Invalid US-ASCII character \"\\xE2\" on line 54 workaround"
date: 2019-07-21
categories:
  - blog
tags:
  - Jekyll
  - update
---

In this blog post I cover the infamous "Invalid US-ASCII character
\"\xE2\" on line 54" error that seems to plague people when trying to
serve their sites locally. OK, I actually don't fix the problem but I
create a workaround.

# The problem

Have you ever ran into this issue?

```shell
Error:  Invalid US-ASCII character "\xE2" on line 54
```

I ran into this issue when trying to serve my jekyll site locally

```
$ jekyll serve
```

And then this happened. 

```shell
Configuration file: /Users/janmeppe/Github-blog/rainymood.github.io/_config.yml
            Source: /Users/janmeppe/Github-blog/rainymood.github.io
       Destination: /Users/janmeppe/Github-blog/rainymood.github.io/_site
 Incremental build: disabled. Enable with --incremental
      Generating...
Invalid theme folder: _sass
      Remote Theme: Using theme mmistakes/minimal-mistakes
       Jekyll Feed: Generating feed for posts
   GitHub Metadata: No GitHub API authentication could be found. Some fields may be missing or have incorrect data.
  Conversion error: Jekyll::Converters::Scss encountered an error while converting 'assets/css/main.scss':
                    Invalid US-ASCII character "\xE2" on line 54
jekyll 3.8.5 | Error:  Invalid US-ASCII character "\xE2" on line 54
exit 1
```

# The solution

After scouring the internet trying many solutions such as the solution presented [here](https://talk.jekyllrb.com/t/how-to-deal-with--sass-converting-errors/911/3) and [this one](https://github.com/jekyll/jekyll/issues/4268), 
I found a very simple solution [here](https://talk.jekyllrb.com/t/locale-problems/1213/2) that works great! 

Create a new file called `Rakefile` with this content

```ruby
task :build do
  system "env LANG=\"en_US.UTF-8\" bundle exec jekyll serve"
end
```

This sets the locale encoding to the correct one and should allow you to serve your site locally, finally!

I spiced mine up a little bit and it looks like this 

```ruby
task :build do
  system "env LANG=\"en_US.UTF-8\" bundle exec jekyll serve -l -o --drafts"
end
```

The `-l` flag turns on live reload, which makes the website rebuild automatically when it detects a change. The `-o` flag opens `localhost` when serving it and the `--drafts` flag allows me to create draft posts so that I can preview them locally before pushing them to my blog. 

Now you can build the website using

```shell
$ rake build
```

Et voilà! 

```shell
Configuration file: /Users/janmeppe/Github-blog/rainymood.github.io/_config.yml
            Source: /Users/janmeppe/Github-blog/rainymood.github.io
       Destination: /Users/janmeppe/Github-blog/rainymood.github.io/_site
 Incremental build: disabled. Enable with --incremental
      Generating...
Invalid theme folder: _sass
      Remote Theme: Using theme mmistakes/minimal-mistakes
       Jekyll Feed: Generating feed for posts
   GitHub Metadata: No GitHub API authentication could be found. Some fields may be missing or have incorrect data.
                    done in 13.275 seconds.
 Auto-regeneration: enabled for '/Users/janmeppe/Github-blog/rainymood.github.io'
    Server address: http://127.0.0.1:4000

```

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
