# Janmeppe.com code 

This repository contains the code and assets of my personal blog which you can find at [janmeppe.com](www.janmeppe.com). 


## Setup

```ruby
rake build
```

Usually we would run the blog using `bundle exec jekyll serve` or simply `build`.

This is a workaround due to a unicode error/bug that I still haven't fixed which you can read more about here:

* [Invalid US-ASCII character “\xE2” on line 54 workaround](https://www.janmeppe.com/blog/invalid-US-ASCII-character/)

## Writing posts

To write: 

* drafts put **undated** posts in the `_drafts/` folder.
* blog posts put **dated** posts in the `_posts/` folder. 

Put all assets in `assets/` in a folder with the same name. 

If you want to see the drafts, serve build/serve Jekyll with the `--draft` flag enabled. 

This flag is by default enabled if you run the blog with `rake build`. 

## Q: How to view your bundler version?

```
cat Gemfile.lock | grep -A 1 "BUNDLED WITH"
BUNDLED WITH
   1.17.3

gem install bundler -v '1.17.3'
```

## Q: How to override settings

Change the settings in `assets/css/main.scss`.

## Q: How to change your home page?

Change settings in `index.html`.

## Resources

* [Minimal mistakes (Jekyll theme used)](https://mmistakes.github.io/minimal-mistakes/)
* [Configuration options](https://mmistakes.github.io/minimal-mistakes/docs/configuration/)
