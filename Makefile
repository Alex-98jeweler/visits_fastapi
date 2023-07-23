all: tests


codestyle:
	flake8 ./src

tests: codestyle
	pytest -v