from datetime import datetime

from boto3.dynamodb.conditions import Key

from ..database import ddb_client


class SensorActivations:
    TableName: str = "sensor_activations"
    table = ddb_client.Table(TableName)
    PKAttributeName: str = "pk"

    async def get_item(self, low_value: str, high_value: str) -> dict:
        response = self.table.query(
            KeyConditionExpression=Key("pk").eq("MOTION_SENSOR") & Key("activated_at").between(low_value, high_value),
            Limit=20,
        )
        return response
