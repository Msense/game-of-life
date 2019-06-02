PYTHON_VERSION    ?= python3.6
VIRTUAL_ENV       ?= ./venv

init_venv:  ## Initialize virtual env
	$(info Initialize virtual env)
ifeq ($(wildcard $(VIRTUAL_ENV)),)
	python -m virtualenv -p $(PYTHON_VERSION) $(VIRTUAL_ENV)
endif
	'$(VIRTUAL_ENV)/bin/pip' install -r requirements.txt

init: init_venv
	$(info Project initialization finished)

test:
    py.test tests

.PHONY: init init_venv test
