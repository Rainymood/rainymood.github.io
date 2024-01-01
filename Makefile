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

post: 
	echo "check if on master"
	echo "git pull"
	echo "get last branch"
	echo "get filename"
	echo "merge last branch into master"
