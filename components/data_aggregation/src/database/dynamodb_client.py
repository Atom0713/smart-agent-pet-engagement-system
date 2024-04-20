import boto3

ddb_client = boto3.resource(
    "dynamodb",
    region_name="us-west-2",
    aws_access_key_id="fghddfghd",
    aws_secret_access_key="dfgeh",
    endpoint_url=" http://localhost:8000",
)
