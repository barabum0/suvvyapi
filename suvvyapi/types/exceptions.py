class SuvvyError(Exception):
    """Error in Suvvy API"""


class InvalidToken(SuvvyError):
    """Invalid Suvvy AI token"""


class CustomChannelDisabled(SuvvyError):
    """Bot custom channel is disabled."""


class NegativeBalance(SuvvyError):
    """Your Suvvy balance is below zero."""


class InvalidFileType(SuvvyError):
    """File type is not supported or invalid."""


class ValidationError(SuvvyError):
    """Validation error."""
