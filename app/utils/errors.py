from fastapi import status

class AppException(Exception):
    """
    Base application exception class
    """
    def __init__(
        self,
        detail: str,
        code: str = "APP_ERROR",
        status_code: int = status.HTTP_400_BAD_REQUEST
    ):
        self.detail = detail
        self.code = code
        self.status_code = status_code
        super().__init__(self.detail)

class NotFoundException(AppException):
    """
    Exception raised when a resource is not found
    """
    def __init__(self, detail: str = "Resource not found", code: str = "NOT_FOUND"):
        super().__init__(detail=detail, code=code, status_code=status.HTTP_404_NOT_FOUND)

class UnauthorizedException(AppException):
    """
    Exception raised when a user is not authorized
    """
    def __init__(self, detail: str = "Unauthorized", code: str = "UNAUTHORIZED"):
        super().__init__(detail=detail, code=code, status_code=status.HTTP_401_UNAUTHORIZED)

class ForbiddenException(AppException):
    """
    Exception raised when a user is forbidden to access a resource
    """
    def __init__(self, detail: str = "Forbidden", code: str = "FORBIDDEN"):
        super().__init__(detail=detail, code=code, status_code=status.HTTP_403_FORBIDDEN)
