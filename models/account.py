from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

from models.transaction import Transaction
from utilities.utils import AccountType


@dataclass
class Account:
    account_id: str
    user_id: str
    account_type: AccountType
    balance: Decimal
    currency: str
    created_at: datetime
    transactions: list[Transaction]
