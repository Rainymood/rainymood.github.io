# Jan Meppe's personal blog

This repository contains the code of Jan Meppe's personal blog. It is built with the [minimal
mistakes](https://mmistakes.github.io/minimal-mistakes/) jekyll theme. Jan's website can be found at [janmeppe.com](www.janmeppe.com)

## How to run locally

```ruby
rake build
```

Instead of using the `bundle exec jekyll serve` (or `build`) we build and run
the website locally using a ruby workaround. 

I have written about this unicode error/bug
 [here](https://www.janmeppe.com/blog/invalid-US-ASCII-character/)
   

## How to write draft posts

To write draft posts put **undated** posts in the `_drafts/` folder and then
build/serve jekyll with `--draft`. Note that this flag is by default enabled
in the `rake build` workaround.

## How do I write blog posts

Because I am a savage I write most of my posts directly in the `_/posts`
folder and throw all the assets in `_assets/`. That is my writing process. 

I have tried writing posts in different editors and things but having to
format it all over again got kind of tiring. This seems to work for me and is simple and stupid enough that I can follow the procedure. 

## Links

* [View my blog here](https://rainymood.github.io/)
* [View configuration options here](https://mmistakes.github.io/minimal-mistakes/docs/configuration/).
