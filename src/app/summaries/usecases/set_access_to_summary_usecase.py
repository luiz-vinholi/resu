import datetime
from src.app import UseCase
from src.infra.repositories import AccessesRepository


class SetAccessToSummaryUseCase(UseCase):
    def __init__(self, ip):
        self._ip = ip
        self._access_limit = 2
        self._accesses_respository = AccessesRepository()

    
    def execute(self):
        access = self._accesses_respository.get_today_access_by_ip(self._ip)
        if access:
            usage = access.get('usage', 0) + 1
            self._accesses_respository.update_accesses(access.id, usage)
        else:
            today = datetime.date.today()
            data = {
                'ip': self._ip,
                'date': today,
                'resource': 'summary',
                'usage': 1,
                'limit': self._access_limit
            }
            self._accesses_respository.create_accesses(data)