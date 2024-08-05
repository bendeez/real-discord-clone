from fastapi import Depends
from app.database_transaction import DatabaseTransactionService


class BaseService:
    def __init__(self, transaction: DatabaseTransactionService = Depends(DatabaseTransactionService)):
        self.transaction = transaction