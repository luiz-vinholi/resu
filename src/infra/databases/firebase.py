import os
from firebase_admin import credentials, initialize_app, firestore, auth


config = credentials.Certificate('firebase-credentials.json')

app = initialize_app(config)
db = firestore.client()
