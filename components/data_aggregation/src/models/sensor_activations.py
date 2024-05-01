import datetime

from ..database import ddb_client


class SensorActivations:
    TableName: str = "sensor_activations"
    table = ddb_client.Table(TableName)
    PKAttributeName: str = "pk"
    SKAttributeName: str = "sk"
    data: dict

    def __init__(self, data: dict) -> None:
        data.update(
            {
                self.PKAttributeName: "MOTION_SENSOR",
                self.SKAttributeName: datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
            }
        )
        self.data = data

    def save(self) -> None:
        response = self.table.put_item(
            Item=self.data,
            TableName=self.TableName,
        )
        print(response)
