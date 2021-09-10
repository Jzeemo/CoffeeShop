import json
import os
from functools import wraps
from urllib.request import urlopen

from flask import _request_ctx_stack, abort, request
from flask.json import jsonify
from icecream import ic
from jose import jwt
from sqlalchemy.sql.expression import true

"""
AuthError Exception
A standardized way to communicate auth failure modes
"""


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


"""
@TODO: implement get_token_auth_header() method
    it should attempt to get the header from the request
        it should raise an AuthError if no header is present
    it should attempt to split bearer and the token
        it should raise an AuthError if the header is malformed
    return the token part of the header
"""

# get the jwt token from header
def get_token_auth_header():

    # check the Authorization include in request header
    if "Authorization" not in request.headers:
        raise AuthError(
            {"code": "not_found", "description": "Bearer Token Not Found"}, 401
        )

    # get the Authorization string
    authString = request.headers["Authorization"]

    # split the the Authorization string by space
    parts = authString.split(" ")

    # check Authorization header is correct format or not
    if parts[0] != "Bearer" or len(parts) != 2:
        raise AuthError(
            {"code": "invalid_token", "description": "Invalid Bearer Token"},
            401,
        )

    jwtToken = parts[1]

    # validate the jwt token format
    components = jwtToken.split(".")
    if len(components) != 3:
        raise AuthError(
            {"code": "invalid_token", "description": "Invalid Bearer Token"},
            401,
        )

    return jwtToken


"""
@TODO: implement check_permissions(permission, payload) method
    @INPUTS
        permission: string permission (i.e. 'post:drink')
        payload: decoded jwt payload

    it should raise an AuthError if permissions are not included in the payload
        !!NOTE check your RBAC settings in Auth0
    it should raise an AuthError if the requested permission string is not in the payload permissions array
    return true otherwise
"""

# This is gonna be python decorator method for checking the permission
def check_permissions(permission, payload):

    # check the payload string whether permission keyword is include or not
    if "permissions" not in payload:
        raise AuthError(
            {
                "code": "invalid_token",
                "description": "Token format is invalid",
            },
            400,
        )

    if permission not in payload["permissions"]:
        raise AuthError(
            {"code": "unauthorized", "description": "Permission not granted"},
            403,
        )

    return True


"""
@TODO: implement verify_decode_jwt(token) method
    @INPUTS
        token: a json web token (string)

    it should be an Auth0 token with key id (kid)
    it should verify the token using Auth0 /.well-known/jwks.json
    it should decode the payload from the token
    it should validate the claims
    return the decoded payload

    !!NOTE urlopen has a common certificate error described here: https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org
"""

# this method to decode the jwt and return payload
def verify_decode_jwt(token):

    # return the config value
    def load_config(file_path):
        with open(file_path, "r") as f:
            return json.load(f)

    # get the config value
    config = load_config("../config.json")

    # get the public key
    jsonurl = urlopen(
        "https://{}/.well-known/jwks.json".format(config["DOMAIN"])
    )

    # get the public key structure
    publickey_list = json.loads(jsonurl.read())

    rsa_key = {}

    for key in publickey_list["keys"]:
        # get the kid value from public key
        if key["kid"] == jwt.get_unverified_header(token)["kid"]:
            rsa_key = {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"],
            }
            break

    if rsa_key:
        try:
            # decode the jwt and return the payload
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=config["ALGORITHMS"],
                audience=config["API_IDENTIFIER"],
                issuer="https://{}/".format(config["DOMAIN"]),
            )

            return payload

        except jwt.ExpiredSignatureError:
            raise AuthError(
                {"code": "token_expired", "description": "Token expired."}, 401
            )

        except jwt.JWTClaimsError as error:
            print(str(error))
            raise AuthError(
                {
                    "code": "invalid_claims",
                    "description": "Incorrect claims. Please, check the audience and issuer.",
                },
                401,
            )
        except Exception:
            raise AuthError(
                {
                    "code": "invalid_header",
                    "description": "Unable to parse authentication token",
                },
                400,
            )
    raise AuthError(
        {
            "code": "invalid_header",
            "description": "Unable to find the appropriate key.",
        },
        400,
    )


"""
STATUS: DONE
@TODO: implement @requires_auth(permission) decorator method
    @INPUTS
        permission: string permission (i.e. 'post:drink')

    it should use the get_token_auth_header method to get the token
    it should use the verify_decode_jwt method to decode the jwt
    it should use the check_permissions method validate claims and check the requested permission
    return the decorator which passes the decoded payload to the decorated method
"""


def requires_auth(permission=""):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):

            # get token from header
            token = get_token_auth_header()

            # get the payload from token
            payload = verify_decode_jwt(token)

            # check the permission from payload
            check_permissions(permission, payload)

            return f(payload, *args, **kwargs)

        return wrapper

    return requires_auth_decorator
