# Janmeppe.com

![](./assets/screenshots/2021-07-14.png)

This repository contains the code, text, and assets of my personal blog which
you can find here at [www.janmeppe.com](www.janmeppe.com). 

## Installation

Clone the repo

```
git clone https://github.com/Rainymood/rainymood.github.io
```

Assuming you have a working installation of [Ruby](https://www.ruby-lang.org/en/downloads/), install the bundler

```
gem install bundler
```

And install all the gems

```
bundle install
```

If this is the first time you are setting up the blog on a new computer. Generate a new
Personal Access Token (PAT) [here](https://github.com/settings/tokens).

## Running the blog (Mac)

Run the blog with

```ruby
rake build
```

Usually we would run the blog using `bundle exec jekyll serve` or simply `build`.

This is a workaround due to a unicode error/bug that I still haven't fixed which you can read more about here:

* [Invalid US-ASCII character “\xE2” on line 54 workaround](https://www.janmeppe.com/blog/invalid-US-ASCII-character/)

## Running the blog (Windows)

Run the blog with 

```
bundle exec jekyll serve --livereload -o --drafts --future
```
## Writing posts

To write: 

* drafts put **undated** posts in the `_drafts/` folder.
* blog posts put **dated** posts in the `_posts/` folder. 

Put all assets in `assets/` in a folder with the same name. 

If you want to see the drafts, serve build/serve Jekyll with the `--draft` flag enabled. 

This flag is by default enabled if you run the blog with `rake build`. 

## Writing posts (in the future)

I want to move towards a workflow where I use branches. I think I want a `draft` branch where I can fuck around and then once I'm done I can just pull it to the main one using a pull request. This would clean up my `main` branch a lot. 

## Docs

I have some docs that I keep in the `docs/` folder. Run and autobuild with:

```bash
sphinx-autobuild docs docs/_build/html
```

## FAQ

Some common issues and solutions can be found in [FAQ.md](FAQ.md).

## Resources

* [Minimal mistakes (Jekyll theme used)](https://mmistakes.github.io/minimal-mistakes/)
* [Configuration options](https://mmistakes.github.io/minimal-mistakes/docs/configuration/)
* [Justin Rummel](https://www.justinrummel.com/page3/): I need to figure out how this guy added pictures 


## Tail for a quick `cat readme.md`

```
bundle exec jekyll serve --livereload -o --drafts --future
```