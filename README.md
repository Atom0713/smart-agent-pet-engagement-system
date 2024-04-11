# smart-agent-pet-engagement-system
System designated to keep pets, locked in apartments, active while their human friends are away.

#3 Design document
https://www.notion.so/ID2012-Ubiquitous-Computing-d95a3c4c89f3437c805b103041c374de

## Prerequisites
- Docker
- python ^3.12
- awscli [optional]

## Local development
To develop locally you will need all components up and running. To avoid poluting your terminal use GNU screen with multiple windows for each component.
### GNU screen
1. Create session:

```screen -S mysession```

2. Create split views and activate them with ```Ctl-a c```
3. Execute command to run components.
### Components
#### Storage
To start local dynamoDB run command below. It will expose dynamoDB service on the http://localhost:8000 endpoint.
```docker-compose up```

To test connection:

```aws dynamodb list-tables --endpoint-url http://localhost:8000```


#### Sensor client
Run senro client:

```make run_sensor_client```

#### Data aggregation service
Run data aggregation tool:

```make run_data_aggregation```


#### Actuator
Run actuator:

```make run_actuator```