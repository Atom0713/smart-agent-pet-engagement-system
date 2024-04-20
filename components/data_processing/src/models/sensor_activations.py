from ..database import ddb_client


class SensorActivations:
    TableName: str = "sensor_activations"
    table = ddb_client.Table(TableName)
    PKAttributeName: str = "pk"

    async def get_item(self) -> any:
        response = self.table.get_item(
            TableName=self.TableName,
        )
        return response
