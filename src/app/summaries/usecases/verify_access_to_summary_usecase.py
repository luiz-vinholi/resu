from src.app import UseCase
from src.infra.repositories import AccessesRepository
from src.app.summaries.errors.expired_resource_access_error import ExpiredResourceAccessError


class VerifyAccessToSummaryUseCase(UseCase):
    def __init__(self, ip):
        self._ip = ip
        self._accesses_repository = AccessesRepository()
    

    def execute(self):
        access = self._accesses_repository.get_today_access_by_id(self._ip)
        if access:
            attempts = access.get('attempts', 0) + 1
            self._accesses_repository.update_access_attempts(access.id, attempts)
            if access.usage >= access.limit:
                raise ExpiredResourceAccessError('summary')
