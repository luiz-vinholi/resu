from src.app import CustomError


class ExpiredResourceAccessError(CustomError):
    def __init__(self, resource: str):
        message = f'The access to {resource} resource has expired by the number of uses in a day'
        code = 'expired-resource-access'
        super().__init__(message=message, code=code)
        self.message = message 
        self.code = code
        self._resource = resource