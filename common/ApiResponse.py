from dataclasses import dataclass

from flask import jsonify
import json


@dataclass
class ApiResponse:
    status: bool = False
    message: str = None
    data: any = None

    def __init__(self):
        pass

    def ok(self, data: any = None, message: str = None) -> json:
        return jsonify({
            'status': True,
            'message': message,
            'data': data
        }), 200

    def error(self, data: any = None, message: str = None) -> jsonify:
        self.status = False
        self.message = message
        self.data = data
        return jsonify(self), 400

    def not_found(self, data: any = None, message: str = None) -> jsonify:
        self.status = False
        self.message = message
        self.data = data
        return jsonify(self), 404

    def internal_server_error(self, data: any = None, message: str = None) -> jsonify:
        self.status = False
        self.message = message
        self.data = data
        return jsonify(self), 500
