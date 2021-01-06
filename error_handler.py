from flask import json, jsonify
from werkzeug.exceptions import InternalServerError, BadRequest, Unauthorized
from app import app
from exception.bad_credentials import BadCredentials
from exception.username_email_exists import UsernameEmailExists


@app.errorhandler(UsernameEmailExists)
def handle_username_email_exists_exception(e):
    return jsonify(e.to_dict())


@app.errorhandler(BadCredentials)
def handle_bad_credentials_exception(e):
    return jsonify(e.to_dict())


@app.errorhandler(InternalServerError)
def handle_internal_server_error_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "message": e.name,
        "success": False,
        "type": 'InternalServerError'
    })
    response.content_type = "application/json"
    return response


@app.errorhandler(BadRequest)
def handle_bad_request_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "message": e.name + ': ' + e.description,
        "success": False,
        "type": 'BadRequest'
    })
    response.content_type = "application/json"
    return response


@app.errorhandler(Unauthorized)
def handle_unauthorized_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "message": e.name + ': ' + e.description,
        "success": False,
        "type": 'Unauthorized'
    })
    response.content_type = "application/json"
    return response
