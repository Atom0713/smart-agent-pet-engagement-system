from ..database import ddb_client


class SensorActivations:
    TableName: str = "sensor_activations"
    table = ddb_client.Table(TableName)
    PKAttributeName: str = "pk"
    SKAttributeName: str = "activated_at"
    data: dict

    def __init__(self, data: dict) -> None:
        pk: str = "MOTION_SENSOR_{}".format(data.get("location", ""))
        data.update(
            {
                self.PKAttributeName: pk,
            }
        )
        self.data = data

    def save(self) -> None:
        _ = self.table.put_item(
            Item=self.data,
            TableName=self.TableName,
        )
