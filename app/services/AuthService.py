import jwt as jwt
from flask import current_app


class AuthService:
    @staticmethod
    def verify_token(token):
        try:
            decoded = jwt.decode(token, current_app.config['SECRET_KEY'])
            return decoded['id']
        except:
            return None
