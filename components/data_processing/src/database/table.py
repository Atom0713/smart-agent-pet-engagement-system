import botocore

from .dynamodb_client import ddb_client


def initialize_db():
    try:
        table = ddb_client.create_table(
            AttributeDefinitions=[
                {"AttributeName": "toy_name", "AttributeType": "S"},
                {"AttributeName": "activate_at", "AttributeType": "S"},
            ],
            TableName="activation_schedule",
            KeySchema=[
                {"AttributeName": "toy_name", "KeyType": "HASH"},
                {"AttributeName": "activate_at", "KeyType": "RANGE"},
            ],
            BillingMode="PAY_PER_REQUEST",
        )
        table.wait_until_exists()
        print("Table status:", table.table_status)
    except botocore.exceptions.ClientError as e:
        if not e.response["Error"]["Code"] == "ResourceInUseException":
            raise e
