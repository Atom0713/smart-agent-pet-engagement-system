from datetime import datetime

from ..database import ddb_client

class ActivationSchedule:
    TableName: str = "activation_schedule"
    table = ddb_client.Table(TableName)
    PKAttributeName: str = "toy_name"
    SKAttributeName: str = "activate_at"
    data: dict

    def __init__(self, activate_at: datetime, toy_name: str) -> None:

        self.data = {
            self.PKAttributeName: toy_name,
            self.SKAttributeName: activate_at.strftime("%m/%d/%Y, %H:%M:%S"),
        }

    def save(self) -> None:
        response = self.table.put_item(Item=self.data)
