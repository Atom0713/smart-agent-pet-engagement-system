import logging
from datetime import datetime, timedelta

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
        now: datetime = datetime.now()
        low_value: str = (now - timedelta(minutes=1)).strftime("%m/%d/%Y, %H:%M:%S")
        response = self.table.query(
            KeyConditionExpression=Key("toy_name").eq("laser")
            & Key(self.SKAttributeName).between(low_value, now.strftime("%m/%d/%Y, %H:%M:%S")),
        )
        return response.get("Items")
