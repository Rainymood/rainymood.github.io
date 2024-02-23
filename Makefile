
MY_VAR := $(shell eval git branch --sort=-committerdate | head -1)

BRANCH := $(shell git rev-parse --abbrev-ref HEAD)
HASH := $(shell git rev-parse HEAD)

build:
	code .
	bundle exec jekyll serve --livereload -o --incremental

blog:
	code .
	bundle exec jekyll serve --livereload -o --incremental

last: 
	code .
	bundle exec jekyll serve --config _config_dev.yml --livereload -o --incremental --limit_posts 1 --profile

new: 
	python new-post.py

publish: 
	git checkout master
	git pull
	echo git merge $(BRANCH)
