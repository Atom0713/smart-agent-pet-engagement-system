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


black:
	poetry run black components

isort:
	poetry run isort components

mypy: mypy_data_aggregation mypy_sensor_client mypy_data_processing mypy_actuator

mypy_sensor_client:
	poetry run mypy components/sensor_client --explicit-package-bases

mypy_data_aggregation:
	poetry run mypy components/data_aggregation --explicit-package-bases

mypy_data_processing:
	poetry run mypy components/data_processing --explicit-package-bases

mypy_actuator:
	poetry run mypy components/actuator --explicit-package-bases

mypy_actuator:
	poetry run mypy components/mobile_app_simulator --explicit-package-bases

flake8:
	poetry run flake8 components
test: mypy flake8
