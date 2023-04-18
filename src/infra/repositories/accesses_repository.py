import datetime
from src.infra.databases.firestore import db


class AccessesRepository:
    def __init__(self):
        self._client = db.collection('accesses')
    
    
    def get_access(self, id):
        doc = self._client.document(id).get()
        return doc


    def get_today_access_by_ip(self, ip):
        today = datetime.date.today()
        today = datetime.datetime.combine(today, datetime.datetime.min.time())
        doc = (self._client
            .where('ip', '==', ip)
            .where('date', '>=', today)
            .get())
        doc = next(iter(doc), None)
        return {'id': doc.id, **doc.to_dict()} if doc else None


    def create_access(self, data):
        _, access = self._client.add(data)
        return access.id
    

    def update_access_attempts(self, id, attempts: int):
        doc_ref = self._client.document(id)
        doc_ref.update({ 'attempts': attempts })

    
    def update_access_usage(self, id, usage: int):
        doc_ref = self._client.document(id)
        doc_ref.update({ 'usage': usage })