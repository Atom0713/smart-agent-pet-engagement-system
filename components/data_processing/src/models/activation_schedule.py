import datetime

from ..database import ddb_client


class ActivationSchedule:
    TableName: str = "activation_schedule"
    table = ddb_client.Table(TableName)
    PKAttributeName: str = "pk"
    SKAttributeName: str = "sk"
    data: dict

    def __init__(self, datetime: datetime, toy_name: str) -> None:

        self.data = {
            self.PKAttributeName: "TEMP",
            self.SKAttributeName: datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
            "activate_at": datetime,
            "toy_name": toy_name,
        }

    def save(self) -> None:
        response = self.table.put_item(
            Item=self.data,
            TableName=self.TableName,
        )
        print(response)
