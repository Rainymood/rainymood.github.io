
MY_VAR := $(shell eval git branch --sort=-committerdate | head -1)

BRANCH := $(shell git rev-parse --abbrev-ref HEAD)
HASH := $(shell git rev-parse HEAD)

ENV_NAME ?= blog
PYTHON_VERSION ?= 3.11
POETRY_VERSION ?= 2.1.1

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
	git merge $(BRANCH) -m "Publish post in $(BRANCH)"
	git push

# Default target when running just 'make'
setup: check-conda force-clean create-env install-deps

# Check if conda is available
check-conda:
	@which conda >/dev/null || (echo "Conda is not installed. Please install Miniconda or Anaconda first." && exit 1)

# Clean existing environment if it exists
clean-env: check-conda
	@echo "Removing existing conda environment '$(ENV_NAME)' if it exists..."
	@conda env remove -n $(ENV_NAME) -y 2>/dev/null || true

# Force clean and remove environment
force-clean: check-conda
	@echo "Force removing conda environment '$(ENV_NAME)'..."
	@conda deactivate 2>/dev/null || true
	@conda env remove -n $(ENV_NAME) -y 2>/dev/null || true
	@rm -rf $(shell conda info --base)/envs/$(ENV_NAME) 2>/dev/null || true

# Create new conda environment
create-env: check-conda
	@echo "Creating new conda environment '$(ENV_NAME)' with Python $(PYTHON_VERSION)..."
	@if [ -d "$(shell conda info --base)/envs/$(ENV_NAME)" ]; then \
		echo "Environment directory exists but not in conda list. Cleaning up..."; \
		$(MAKE) force-clean; \
	fi
	@conda create --name $(ENV_NAME) python=$(PYTHON_VERSION) -y

# Install dependencies
install-deps: check-conda
	@echo "Installing dependencies (Poetry $(POETRY_VERSION))..."
	@if [ ! -d "$(shell conda info --base)/envs/$(ENV_NAME)" ]; then \
		echo "Error: Environment '$(ENV_NAME)' does not exist. Run 'make create-env' first."; \
		exit 1; \
	fi
	@echo "source $$(conda info --base)/etc/profile.d/conda.sh && \
	conda activate $(ENV_NAME) && \
	pip install poetry==$(POETRY_VERSION) && \
	poetry config virtualenvs.create false && \
	poetry install --no-root" | bash

# Activate the environment (note: this needs to be sourced, not run directly)
activate:
	@echo "Run this command to activate the environment:"
	@echo "source $$(conda info --base)/etc/profile.d/conda.sh && conda activate $(ENV_NAME)"