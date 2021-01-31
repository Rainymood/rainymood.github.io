# Janmeppe.com code 

This repository contains the code and assets of my personal blog which you can find at [janmeppe.com](www.janmeppe.com). 

It uses the [minimal
mistakes](https://mmistakes.github.io/minimal-mistakes/) jekyll theme with some minor tweaks.

## Setup

```ruby
rake build
```

Usually we would run the blog using `bundle exec jekyll serve` or `build`.
This is a workaround due to a unicode error/bug that I still haven't fixed.
Read about that [here](https://www.janmeppe.com/blog/invalid-US-ASCII-character/).

## Draft 

To write draft posts put **undated** posts in the `_drafts/` folder and then
build/serve jekyll with `--draft`.

This flag is by default enabled if you run with `rake build`. 

## Blog posts

Usually I don't bother with draft posts and write them directly in `_/posts`. All assets go in `assets/`. 

## Links

* [View my blog here](https://rainymood.github.io/)
* [View configuration options here](https://mmistakes.github.io/minimal-mistakes/docs/configuration/).


## View bundler

```
cat Gemfile.lock | grep -A 1 "BUNDLED WITH"
BUNDLED WITH
   1.17.3

gem install bundler -v '1.17.3'
```

## How to override settings

Change the settings in `assets/css/main.scss`.

## How to change your home page?

Change settings in `index.html`.