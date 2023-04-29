from pydantic import BaseModel, EmailStr, validator
from src.infra.repositories import AuthRepository


def set_auth_router(app):
    auth_repository = AuthRepository()

    class CreateSessionBody(BaseModel):
        email: EmailStr
        password: str

    @app.post('/auths/sessions')
    def create_session(body: CreateSessionBody):
        user = auth_repository.create_session_with_email_and_password(
            email=body.email,
            password=body.password
        )
        return user


    class CreateUserBody(BaseModel):
        name: str
        email: EmailStr
        password: str

        @validator('name')
        def check_name_length(cls, name):
            if len(name) <= 3:
                raise ValueError('The "name" field in body must be at least 3 characters')
            return name
    

    @app.post('/auths/users')
    def create_user(body: CreateUserBody):
        auth_repository.create_user_with_email_and_password(
            email=body.email,
            password=body.password,
            name=body.name
        )
        return None