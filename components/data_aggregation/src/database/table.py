import botocore

from .dynamodb_client import ddb_client


def initialize_db():
    try:
        table = ddb_client.create_table(
            AttributeDefinitions=[
                {"AttributeName": "pk", "AttributeType": "S"},
                {"AttributeName": "activated_at", "AttributeType": "S"},
            ],
            TableName="sensor_activations",
            KeySchema=[
                {"AttributeName": "pk", "KeyType": "HASH"},
                {"AttributeName": "activated_at", "KeyType": "RANGE"},
            ],
            BillingMode="PAY_PER_REQUEST",
        )
        table.wait_until_exists()
        print("Table status:", table.table_status)
    except botocore.exceptions.ClientError as e:
        if not e.response["Error"]["Code"] == "ResourceInUseException":
            raise e
