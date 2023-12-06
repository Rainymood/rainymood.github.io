build:
	code .
	bundle exec jekyll serve --livereload -o --incremental

blog:
	code .
	bundle exec jekyll serve --livereload -o --incremental

last: 
	bundle exec jekyll serve --config _config_dev.yml --livereload -o --incremental --limit_posts 1 --profile