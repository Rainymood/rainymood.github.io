
MY_VAR := $(shell eval git branch --sort=-committerdate | head -1)

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

# publish: 
# 	git checkout master
# 	git pull
# 	git merge $(MY_VAR) -m "Merge branch $(MY_VAR)" && git push