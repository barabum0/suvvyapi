import re
from typing import Optional


class InvalidAPITokenError(BaseException):
    """Raised, when API token is invalid"""


class NegativeBalanceError(BaseException):
    """Raised, when your Suvvy AI balance is under zero"""

    balance: Optional[int] = None

    @classmethod
    def from_detail(cls, detail: str):
        exc = cls("Your balance is under zero")
        balance = int(
            re.search(pattern="(\(\d*\))", string=detail).group(0).strip("()")
        )
        exc.balance = balance
        return exc


class HistoryStoppedError(BaseException):
    """Raised, when history is marked as stopped"""


class HistoryNotFoundError(BaseException):
    """Raised, when history with this unique id is not found"""


class HistoryTooLongError(BaseException):
    """Raised, when history is too long to process"""


class MessageLimitExceededError(BaseException):
    """Raised, when message limit for that instance is exceeded"""


class UnknownAPIError(BaseException):
    """Raised, when WE DON'T KNOW WHAT HAPPENED"""


class InternalAPIError(BaseException):
    """Raised, when internal api error occurred"""
