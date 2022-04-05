MODULE      = ceader
LIBS        = $(MODULE) tests
PYTHON      = poetry run python
PRECOMMIT   = poetry run pre-commit

FILES_DIR = data
HEADER_PATH = tests/data/header.txt
EXTENSIONS = .py .txt .go .yaml .sh .html .c++ .cpp
PARALLELISM ?= 1 #NotImplemented


.PHONY: clean fmt lint test init shell run-stack down-stack scrape

# first arg is mode
define run_ceader
		${PYTHON} -m ${MODULE} --mode $(1)  \
		--files-dir ${FILES_DIR} --header-path ${HEADER_PATH} \
		--extensions-list ${EXTENSIONS} --parallelism ${PARALLELISM} \
		--debug
endef


.git/hooks/pre-commit:
	@${PRECOMMIT} install
	@${PRECOMMIT} autoupdate
	@touch $@

pyproject.toml:
	@touch $@

poetry.lock: pyproject.toml
	@poetry env use "$(shell which python)"
	@poetry install
	@touch $@

init: poetry.lock .git/hooks/pre-commit

shell: poetry.lock
	@poetry shell

clean:
	@find . -type f -name "*.pyc" -delete
	@rm -f poetry.lock

lint: poetry.lock
	@${PYTHON} -m black ${LIBS}
	@${PYTHON} -m autoflake --in-place --recursive --remove-all-unused-imports --expand-star-imports ${LIBS}
	@${PYTHON} -m isort ${LIBS}
	@${PYTHON} -m mypy ${LIBS}
	@${PYTHON} -m bandit --configfile .bandit.yaml --recursive ${LIBS}


add_header: poetry.lock
	@$(call run_ceader, add_header)

remove_header: poetry.lock
	@$(call run_ceader, remove_header)
