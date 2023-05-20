from flask import Blueprint, jsonify
from flask.views import MethodView
from flask_restful.representations import json

from common.ApiResponse import ApiResponse


def ok(data: any = None, message: str = None) -> json:
    status = True
    message = message
    data = data
    return jsonify({
        'status': status,
        'message': message,
        'data': data
    }), 200


def error(data: any = None, message: str = None) -> json:
    status = False
    message = message
    data = data
    return jsonify({
        'status': status,
        'message': message,
        'data': data
    }), 400


def not_found(data: any = None, message: str = None) -> json:
    status = False
    message = message
    data = data
    return jsonify({
        'status': status,
        'message': message,
        'data': data
    }), 404


def internal_server_error(data: any = None, message: str = None) -> json:
    status = False
    message = message
    data = data
    return jsonify({
        'status': status,
        'message': message,
        'data': data
    }), 500


class BaseController(MethodView):
    def __init__(self):
        pass
