from boto3.dynamodb.conditions import Attr, Key

from ..database import ddb_client


class SensorActivations:
    TableName: str = "sensor_activations"
    table = ddb_client.Table(TableName)
    PKAttributeName: str = "pk"

    async def get_item(self) -> dict:
        response = self.table.query(
            KeyConditionExpression=Key("pk").eq("MOTION_SENSOR"),
        )
        return response
