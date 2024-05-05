from ..database import ddb_client


class ActivationSchedule:
    TableName: str = "activation_schedule"
    table = ddb_client.Table(TableName)
    PKAttributeName: str = "toy_name"
    SKAttributeName: str = "activate_at"
    data: dict

    def __init__(self, data: dict) -> None:
        self.data = data

    async def save(self) -> None:
        _ = self.table.put_item(Item=self.data)
