build:
	poetry lock

run_sensor_client:
	poetry run python components/sensor_client/src/sensor_client.py
run_data_aggregation:
	poetry run uvicorn components.data_aggregation.src.app:app --reload

black:
	poetry run black components

isort:
	poetry run isort components

mypy: mypy_data_aggregation mypy_sensor_client

mypy_sensor_client:
	poetry run mypy components/sensor_client

mypy_data_aggregation:
	poetry run mypy components/data_aggregation

flake8:
	poetry run flake8 components/sensor_client components/data_aggregation components/actuator

test: mypy flake8
