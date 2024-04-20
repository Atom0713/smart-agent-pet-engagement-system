from ..database import ddb_client


class TempModel:
    TableName: str = "temp_name"
    table = ddb_client.Table(TableName)
    PKAttributeName: str = "pk"
    data: dict

    def __init__(self, data: dict) -> None:
        data.update({self.PKAttributeName: "TEMP"})
        self.data = data

    def save(self) -> None:
        response = self.table.put_item(
            Item=self.data,
            TableName=self.TableName,
        )
        print(response)
