import json
import os

from flask import Flask, abort, jsonify, redirect, request, url_for
from flask_cors import CORS
from icecream import ic

from .auth.auth import AuthError, requires_auth
from .database.models import Drink, db_drop_and_create_all, setup_db

HOST = "127.0.0.1"
PORT = 5000

app = Flask(__name__)
setup_db(app)
CORS(app)

"""
@TODO: uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
!! Running this funciton will add one
"""
db_drop_and_create_all()

"""
@TODO: implement endpoint
    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
"""


@app.route("/drinks")
def get_drinks():

    # get all drink object
    drinks = Drink.query.all()

    # get the drink short format
    drinks_list = [drink.short() for drink in drinks]

    return jsonify({"success": True, "drinks": drinks_list})


"""
STATUS: DONE
@TODO: implement endpoint
    GET /drinks-detail
        it should require the 'get:drinks-detail' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
"""


@app.route("/drinks-detail")
@requires_auth("get:drinks-detail")
def get_drinks_detail(payload):

    # get all drink object
    drinks = Drink.query.all()

    # get the drink long format
    drinks = [drink.long() for drink in drinks]

    return jsonify({"success": True, "drinks": drinks})


"""
STATUS: DONE
@TODO: implement endpoint
    POST /drinks
        it should create a new row in the drinks table
        it should require the 'post:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink
        or appropriate status code indicating reason for failure
"""


@app.route("/drinks", methods=["POST"])
@requires_auth("post:drinks")
def create_drinks(payload):

    # get the request body
    request_body = request.get_json()

    # get request data
    title = request_body["title"]
    recipe = json.dumps(request_body["recipe"])

    # check request data is valid or not
    if (title is None) or (recipe is None):
        abort(422)

    # add new drink
    drink = Drink(title, recipe)
    drink.insert()

    return jsonify({"success": True, "drinks": drink.long()})


"""
STATUS: DONE
@TODO: implement endpoint
    PATCH /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
        or appropriate status code indicating reason for failure
"""


@app.route("/drinks/<int:drink_id>", methods=["PATCH"])
@requires_auth("patch:drinks")
def update_drinks(payload, drink_id):

    # check the update drink id , return 400 if none
    if drink_id is None:
        abort(400)

    # get the drink by id
    drink = Drink.query.filter(Drink.id == drink_id).one_or_none()

    # return None, If there is no drink by id
    if drink is None:
        abort(404)

    request_body = request.get_json()

    drink.title = (
        request_body["title"] if "title" in request_body else drink.title
    )
    drink.recipe = (
        request_body["recipe"] if "recipe" in request_body else drink.recipe
    )

    drink.update()

    return jsonify({"success": True, "drinks": [drink.short()]})


"""
STATUS: DONE
@TODO: implement endpoint
    DELETE /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
"""


@app.route("/drinks/<int:drink_id>", methods=["DELETE"])
@requires_auth("delete:drinks")
def delete_drinks(payload, drink_id):

    # check the update drink id , return 400 if none
    if drink_id is None:
        abort(400)

    # get the drink by id
    drink = Drink.query.filter(Drink.id == drink_id).one_or_none()

    # return None, If there is no drink by id
    if drink is None:
        abort(404)

    drink.delete()

    return jsonify({"success": True, "drinks": drink_id})


# Error Handling
"""
Example error handling for unprocessable entity
"""


@app.errorhandler(400)
def bad_request(error):
    return (
        jsonify({"success": False, "error": 400, "message": "Bad Request!"}),
        400,
    )


@app.errorhandler(401)
def unauthorized(error):
    return (
        jsonify({"success": False, "error": 401, "message": "Unauthorized!"}),
        401,
    )


@app.errorhandler(403)
def forbidden(error):
    return (
        jsonify(
            {
                "success": False,
                "error": 403,
                "message": "Forbidden!",
            }
        ),
        403,
    )


@app.errorhandler(422)
def unprocessable(error):
    return (
        jsonify({"success": False, "error": 422, "message": "Unprocessable!"}),
        422,
    )


"""
@TODO: implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False,
                    "error": 404,
                    "message": "resource not found"
                    }), 404
"""

"""
@TODO: implement error handler for 404
    error handler should conform to general task above
"""


@app.errorhandler(404)
def not_found(error):
    return (
        jsonify(
            {"success": False, "error": 404, "message": "Resource Not Found!"}
        ),
        404,
    )


"""
@TODO: implement error handler for AuthError
    error handler should conform to general task above
"""


@app.errorhandler(AuthError)
def handle_auth_error(error):
    return jsonify(error.error), error.status_code
