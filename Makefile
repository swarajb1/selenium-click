SHELL := /bin/bash

PYTHON=$(shell which python3)
ifeq ($(PYTHON),)
	PYTHON=$(shell which python)
	ifneq ($(PYTHON),)
		ifeq ($(shell $(PYTHON) -V | grep '^Python 3'),)
			PYTHON=
		endif
	endif
endif


PYTHON = ./.venv/bin/python

WORKDIR=selenium_click


install:  ## Install poetry to run on local
	$(MAKE) generate_dot_env
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install poetry
	$(PYTHON) -m poetry install
	poetry run pre-commit install

run: ## run the program
	clear
	PYTHONPATH=$(WORKDIR)/ $(PYTHON) selenium_click/main.py

clean:
	rm -rf __pycache__



generate_dot_env:  ## Create .env from template if it does not exist.
	@if [[ ! -e .env ]]; then \
		cp .env.template .env; \
	fi
