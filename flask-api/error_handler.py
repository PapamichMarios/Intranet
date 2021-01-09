from flask import json, jsonify
from werkzeug.exceptions import InternalServerError, BadRequest, Unauthorized
from app import app
from exception.bad_credentials import BadCredentials
from exception.resource_not_found import ResourceNotFound
from exception.username_email_exists import UsernameEmailExists


@app.errorhandler(ResourceNotFound)
def handle_resource_not_found_exception(e):
    return jsonify(e.to_dict()), e.code


@app.errorhandler(UsernameEmailExists)
def handle_username_email_exists_exception(e):
    return jsonify(e.to_dict()), e.code


@app.errorhandler(BadCredentials)
def handle_bad_credentials_exception(e):
    return jsonify(e.to_dict()), e.code


@app.errorhandler(InternalServerError)
def handle_internal_server_error_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "message": e.name,
        "success": False,
        "type": 'InternalServerErrorException'
    })
    response.content_type = "application/json"
    return response, e.code


@app.errorhandler(BadRequest)
def handle_bad_request_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "message": e.name + ': ' + e.description,
        "success": False,
        "type": 'BadRequestException'
    })
    response.content_type = "application/json"
    return response, e.code


@app.errorhandler(Unauthorized)
def handle_unauthorized_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "message": e.name + ': ' + e.description,
        "success": False,
        "type": 'UnauthorizedException'
    })
    response.content_type = "application/json"
    return response, e.code
