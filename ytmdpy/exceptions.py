__all__ = (
    "YTMDPyException",
    "APIError",
    "AuthorizationError",
)


class YTMDPyException(Exception):
    """Base exception class for ytmdpy."""

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


class APIError(YTMDPyException):
    """Exception raised when an API error occurs."""

    def __init__(self, message: str) -> None:
        super().__init__(message)


class AuthorizationError(APIError):
    """Exception raised when authorization fails."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
