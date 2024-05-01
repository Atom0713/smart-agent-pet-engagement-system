from .dynamodb_client import ddb_client
from .table import initialize_db

__all__: list[str] = ["ddb_client", "initialize_db"]
