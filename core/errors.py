from flask import jsonify
from functools import wraps


def handle_errors(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            return jsonify({'message': str(e)}), 500

    return decorated_function
