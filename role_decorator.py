from functools import wraps
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt


def role_required(role):

    def decorator(fn):

        @wraps(fn)
        @jwt_required()
        def wrapper(*args, **kwargs):

            claims = get_jwt()

            if claims["role"].lower() != role.lower():

                return jsonify({

                    "message": "Access Denied"

                }), 403

            return fn(*args, **kwargs)

        return wrapper

    return decorator