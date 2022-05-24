install:
	poetry install

build:
	poetry build

publish:
	poetry run --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

uninstall:
	pip uninstall hexlet-code