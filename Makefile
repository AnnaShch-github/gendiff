install:
	poetry install

build:
	poetry build

publish:
	poetry run --dry-run

package-install:
	python3 -m pip install dist/*.whl --force-reinstall

lint:
	poetry run flake8 gendiff

uninstall:
	pip uninstall hexlet-code

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff