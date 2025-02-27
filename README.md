# Janmeppe.com

This repository contains the code, text, and assets of my personal blog which
you can visit at [www.janmeppe.com](www.janmeppe.com). 

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

If this is the first time you are setting up the blog on a new computer generate a new Personal Access Token (PAT) [here](https://github.com/settings/tokens).

## Running the blog (Windows)

Run the blog with 

```bash
make blog
```



## Running the blog (Mac)

Run the blog with

```ruby
rake build
```

Ideally we would use `bundle exec jekyll serve` or `build` but [this](https://www.janmeppe.com/blog/invalid-US-ASCII-character/) is the reason why we can not do this. 

## Writing posts

```bash
git checkout -b 2023-12-09-new-post
make new
make last
```

Should result in 

```
Input name of title (ctrl + C to cancel): dan harmon writing advice
foldername:  2022-05-20-dan-harmon-writing-advice
filename:  2022-05-20-dan-harmon-writing-advice.md
Successfully created assets\2022-05-20-dan-harmon-writing-advice
Successfully created _posts\2022-05-20-dan-harmon-writing-advice.md
```

Start writing, push to this branch, once you are done make a PR to the main branch and (squash) merge it in. 

## Speeding things up... 

Jekyll gets slow when you have lots of pages. I got sick and tired of having to
wait 20 seconds to see an update to any blog post. Run `make last` to use the
`_config_dev.yml` and only build the latest post. This also disables the other
`_pages` because those contain relative `{% post_url %}` links which break if
the posts don't exist.

```
$ make last
bundle exec jekyll serve --config _config_dev.yml --livereload -o --incremental --limit_posts 1 --profile
... 
      Regenerating: 1 file(s) changed at 2023-12-06 07:55:56
                    2023-08-30-i-recently-passed-the-aws-solution-architect-associate-exam-aws-saa-c03-heres-how-i-did-it.md

                    ...done in 3.2591694 seconds.
```

Still not as snappy as I want it, but sure as hell a lot better than >20 seconds.

* https://deku.posstree.com/en/jekyll/preview-speed-up/

## Changing the styling

Edit `assets\css\main.scss`

## Resources

* [Minimal mistakes (Jekyll theme used)](https://mmistakes.github.io/minimal-mistakes/)
* [Configuration options](https://mmistakes.github.io/minimal-mistakes/docs/configuration/)
* [Justin Rummel](https://www.justinrummel.com/page3/): I need to figure out how this guy added pictures 
* https://www.fabriziomusacchio.com/blog/
  * Simple view is awesome
  * Has images

## Tail for `cat readme.md`

I should probably make an alias for this but I'm too lazy so I usually do `cat readme.md` and then copy paste this command to start my blog locally.

The `--incremental` flag is a lifesaver. 

```
bundle exec jekyll serve --livereload -o --incremental
```