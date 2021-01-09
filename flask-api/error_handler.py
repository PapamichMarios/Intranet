from flask import json, jsonify
from werkzeug.exceptions import InternalServerError, BadRequest, Unauthorized
from app import app, jwt
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


# Using the expired_token_loader decorator, we will now call
# this function whenever an expired but otherwise valid access
# token attempts to access an endpoint
@jwt.expired_token_loader
def my_expired_token_callback(expired_token):
    token_type = expired_token['type']
    return jsonify({
        'code': 401,
        'message': 'The {} token has expired'.format(token_type),
        "success": False,
        "type": 'UnauthorizedException'
    }), 401
