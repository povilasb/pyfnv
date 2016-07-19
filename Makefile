python := python3

virtualenv_dir := pyenv
pip := $(virtualenv_dir)/bin/pip
pytest := $(virtualenv_dir)/bin/py.test
pylint := $(virtualenv_dir)/bin/pylint
coverage := $(virtualenv_dir)/bin/coverage


lint:
	$(pylint) fnv/
.PHONY: lint

test: $(virtualenv_dir)
	PYTHONPATH=$(PYTHONPATH):. $(coverage) run \
		--source fnv $(pytest) -s tests
	$(coverage) report -m
.PHONY: test

$(virtualenv_dir): requirements/dev.txt requirements/prod.txt
	virtualenv $@ --python=python3

	for r in $^ ; do \
		$(pip) install -r $$r ; \
	done
