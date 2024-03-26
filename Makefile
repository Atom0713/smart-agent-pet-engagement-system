build:
	@echo run
run_sensor_client:
	poetry --directory src/sensor_client run python src/sensor_client/src/sensor_client.py

run:
	@echo run

black:
	poetry run black src

isort:
	poetry run isort src

mypy:
	poetry run mypy src

flake8:
	poetry run flake8 src

test: mypy flake8
