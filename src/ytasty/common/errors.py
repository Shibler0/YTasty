NOT_FOUND_MESSAGE = "{resource} avec l'id {resource_id} est introuvable"


class AppError(Exception):
    pass


class NotFoundError(AppError):

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class UnauthorizedError(AppError):

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class ForbiddenError(AppError):

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class BadRequestError(AppError):

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)
