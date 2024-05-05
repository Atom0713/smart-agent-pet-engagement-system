from boto3.dynamodb.conditions import Key

from ..database import ddb_client


class SensorActivations:
    TableName: str = "sensor_activations"
    table = ddb_client.Table(TableName)
    PKAttributeName: str = "pk"

    async def get_item(self, low_value: str, high_value: str, location: str) -> dict:
        response = self.table.query(
            KeyConditionExpression=Key("pk").eq(f"MOTION_SENSOR_{location}")
            & Key("activated_at").between(low_value, high_value),
            Limit=20,
        )
        return response
