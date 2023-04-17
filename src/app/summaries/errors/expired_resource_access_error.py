class ExpiredResourceAccessError(Exception):
    def __init__(self, resource: str):
        message = f'The access to {resource} resource has expired by the number of uses in a day'
        super().__init__(message)
        self.message = message 
        self.code = 'expired-resource-access'
        self._resource = resource


    def __str__(self):
        return self.message