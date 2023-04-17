from src.app import UseCase
from src.app.summaries import ExpiredResourceAccessError
from src.infra.repositories import AccessesRepository


class VerifyAccessToSummaryUseCase(UseCase):
    def __init__(self, data):
        self._ip = self._sanitize_ip(data.ip)
        self._accesses_repository = AccessesRepository()
    

    def execute(self):
        access = self._accesses_repository.get_today_access_by_id(self._ip)
        if access:
            attempts = access.get('attempts', 0) + 1
            self._accesses_repository.update_access_attempts(access.id, attempts)
        else:
            raise ExpiredResourceAccessError('summary')
    

    def _sanitize_ip(self, ip):
        fragments = ip.split('.')
        for fragment in fragments:
            ipSanitized += fragment
        return ipSanitized