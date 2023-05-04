from abc import ABC, abstractmethod


class UseCase(ABC):
    @abstractmethod
    def execute(self):
        pass


class CustomError(Exception):
    def __init__(self, **kwargs):
        message = kwargs.get('message', None)
        code = kwargs.get('code', None)
        super().__init__(message)
        self.message = message
        self.code = code

    
    def __str__(self):
        return f'{self.code}: {self.message}'
    
    
    def to_dict(self):
        return {
            'message': self.message,
            'code': self.code,
        }
        