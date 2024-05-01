import logging

from boto3.dynamodb.conditions import Key

from ..database import ddb_client

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")


class ActivationSchedule:
    TableName: str = "activation_schedule"
    table = ddb_client.Table(TableName)
    PKAttributeName: str = "toy_name"
    SKAttributeName: str = "activate_at"
    data: dict

    async def get_item(self) -> dict:
        # how to query?
        response = self.table.query(
            KeyConditionExpression=Key("toy_name").eq("laser"),
        )
        return response.get("Items")
