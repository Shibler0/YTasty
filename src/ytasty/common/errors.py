NOT_FOUND_MESSAGE = "{resource} avec l'id {resource_id} est introuvable"


class AppError(Exception):
    """Erreur de base de l'application."""


class NotFoundError(AppError):
    """Erreur levee lorsqu'une ressource n'existe pas."""

    def __init__(self, resource: str, resource_id):
        self.resource = resource
        self.resource_id = resource_id

        message = NOT_FOUND_MESSAGE.format(
            resource=resource,
            resource_id=resource_id,
        )

        super().__init__(message)
