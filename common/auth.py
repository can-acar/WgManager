# auth.py

from flask import request, jsonify
from functools import wraps

from app.services.AuthService import AuthService


def auth_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token or not AuthService.verify_token(token):
            return jsonify({'message': 'Unauthorized'}), 401
        return f(*args, **kwargs)

    return decorated_function
