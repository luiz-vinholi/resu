import json
import requests
import os
from src.infra.databases.firebase import auth


class AuthRepository:
    def __init__(self):
        self._url = os.getenv('FIREBASE_ACCOUNT_API_URL')
        self._api_key = os.getenv('FIREBASE_WEB_API_KEY')


    def create_user_with_email_and_password(self, **kwargs):
        user = auth.create_user(
            email=kwargs.get('email'),
            password=kwargs.get('password'),
            display_name=kwargs.get('name')
        )
        return user.uid

    
    def create_session_with_email_and_password(self, **kwargs):
        data = json.dumps({
            'email': kwargs.get('email'),
            'password': kwargs.get('password'),
            'return_secure_token': True
        })
        response = requests.post(
            f'{self._url}:signInWithPassword',
            params={'key': self._api_key},
            data=data
        )
        response = response.json()
        response = {
            'user_name': response['displayName'],
            'token': response['idToken'],
            'refresh_token': response['refreshToken'],
            'expires_in': response['expiresIn'],
        }
        return response


    def validate_session(self, token):
        user = auth.verify_id_token(token)
        return user