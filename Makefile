build:
	poetry lock

run_sensor_client:
	poetry run python src/sensor_client/src/sensor_client.py
run_data_aggregation:
	poetry run uvicorn src.data_aggregation.src.app:app --reload

black:
	poetry run black src

isort:
	poetry run isort src

mypy:
	poetry run mypy src

flake8:
	poetry run flake8 src

test: mypy flake8
