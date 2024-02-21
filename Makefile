
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

<<<<<<< HEAD
publish: 
	git checkout master
	git pull
	git merge $(MY_VAR) -m "Merge branch $(MY_VAR)"
=======
# publish: 
# 	git checkout master
# 	git pull
# 	git merge $(MY_VAR) -m "Merge branch $(MY_VAR)" && git push
>>>>>>> 433f72e102d661ebe317c654464b0ba6d6145f60
