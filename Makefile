build:
	poetry lock

run_sensor_client:
	poetry run python components/sensor_client/src/sensor_client.py

run_data_aggregation:
	poetry run uvicorn components.data_aggregation.src.app:app

run_data_processing:
	poetry run python components/data_processing/src/data_processing.py

run_actuator:
	poetry run python components/actuator/src/actuator.py

run_mobile_app_simulator:
	poetry run uvicorn --port 8005 components.mobile_app_simulator.src.app:app

run_house_toys_simulator:
	poetry run uvicorn --port 8006 components.house_toys_simulator.src.app:app

black:
	poetry run black components common

isort:
	poetry run isort components common

mypy: 
	poetry run mypy components common  --explicit-package-bases

flake8:
	poetry run flake8 components

test: mypy flake8
