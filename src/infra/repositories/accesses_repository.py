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
        doc = (self._client
            .where('ip', '==', ip)
            .where('date', '>=', today)
            .get())
        return doc.to_dict() if doc.exists else None


    def create_access(self, data):
        _, access = self._client.add(data)
        return access.id
    

    def update_access_attempts(self, id, attempts: int):
        doc_ref = self._client.document(id)
        doc_ref.update({ 'attempts': attempts })

    
    def update_access_attempts(self, id, usage: int):
        doc_ref = self._client.document(id)
        doc_ref.update({ 'usage': usage })