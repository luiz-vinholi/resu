from firebase_admin import credentials, initialize_app, firestore

config = credentials.Certificate('firebase-credentials.json')

app = initialize_app(config)
db = firestore.client()
