build:
	@echo run

run:
	@echo run

black:
	@echo run

isort:
	@echo run

mypy:
	@echo run

flake8:
	@echo run

test: mypy flake8
	@echo run