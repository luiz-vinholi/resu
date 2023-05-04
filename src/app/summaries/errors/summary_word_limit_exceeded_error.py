from src.app import CustomError


class SummaryWordLimitExceededError(CustomError):
    def __init__(self):
        message = 'Quantity of words in text to summarize is above the allowed'
        code = 'summary-word-limit-exceeded'
        super().__init__(message=message, code=code)
        self.message = message 
        self.code = code