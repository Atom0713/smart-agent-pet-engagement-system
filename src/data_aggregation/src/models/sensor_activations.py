from boto3.resources.base import ServiceResource

class SensorActivations:
    TableName: str = "sensor_activations"

    def __init__(self, ddb_client: ServiceResource) -> None:
        self._db: ServiceResource = ddb_client
        self.table = self._db.Table(self.TableName)
    
    def save(self) -> None:
        pass
        # self._db.put_item()