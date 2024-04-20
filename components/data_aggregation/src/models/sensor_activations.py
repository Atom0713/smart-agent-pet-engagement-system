from boto3.resources.base import ServiceResource

from ..database import ddb_client


class SensorActivations:
    TableName: str = "sensor_activations"
    table = ddb_client.Table(TableName)
    PKAttributeName: str = "pk"
    data: dict

    def __init__(self, data: dict) -> None:
        data.update({self.PKAttributeName: "SENSOR"})
        self.data = data

    def save(self) -> None:
        response = self.table.put_item(
            Item=self.data,
            TableName=self.TableName,
        )
        print(response)
