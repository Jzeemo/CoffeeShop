import os
from flask import Flask, request, jsonify, abort, redirect, url_for
import json
from flask_cors import CORS
from icecream import ic
from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

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

# ROUTES
"""
STATUS: DONE
@TODO: implement endpoint
    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
"""


@app.route("/drinks")
def get_drinks():
    """Get a list of drinks in short form"""
    try:

        #get all drink object
        drinks = Drink.query.all()
        
        drinks_list = [drink.short() for drink in drinks]

        return jsonify({"success": True, "drinks": drinks_list})

    except Exception:        
        abort(500)


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
    """Get a list of drinks in long form"""    

    try:

        #get all drink
        drinks = Drink.query.all()

        drinks = [drink.long() for drink in drinks]

        return jsonify({"success": True, "drinks": drinks})

    except Exception:        
        abort(500)


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
    """Add a new drink"""

    try:
        request_body = request.get_json()
        title = request_body["title"]
        recipe = json.dumps(request_body["recipe"])
        drink = Drink(title, recipe)        
        drink.insert()

        return jsonify({"success": True, "drinks": drink.long()}), 200
    except Exception:
        abort(400)


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
    """Update an existing drink"""

    #check the update drink id , return 400 if none
    if drink_id is None:
        abort(400)
    
    #get the drink by id
    drink = Drink.query.filter(Drink.id == drink_id).one_or_none()

    #return None, If there is no drink by id
    if drink is None:
        abort(404)

    try:
        reqBody = request.get_json()
        if "title" in reqBody:
            drink.title = reqBody["title"]
        if "recipe" in reqBody:
            drink.recipe = reqBody["recipe"]
        drink.update()
        return jsonify({"success": True, "drinks": [drink.short()]})

    except Exception:        
        abort(500)


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
    """Delete an existing drink"""

    #check the update drink id , return 400 if none
    if drink_id is None:
        abort(400)
    
    #get the drink by id
    drink = Drink.query.filter(Drink.id == drink_id).one_or_none()

    #return None, If there is no drink by id
    if drink is None:
        abort(404)

    try:

        drink.delete()
        return jsonify({"success": True, "drinks": drink_id})

    except Exception:        
        abort(500)


# Error Handling
"""
Example error handling for unprocessable entity
"""


@app.errorhandler(400)
def bad_request(error):
    return (
        jsonify({"success": False, "error": 400, "message": "bad request"}),
        400,
    )


@app.errorhandler(401)
def unauthorized(error):
    return (
        jsonify({"success": False, "error": 401, "message": "unauthorized"}),
        401,
    )


@app.errorhandler(403)
def forbidden(error):
    return (
        jsonify(
            {
                "success": False,
                "error": 403,
                "message": "no permission to access this",
            }
        ),
        403,
    )


"""
STATUS: DONE
@TODO: implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False,
                    "error": 404,
                    "message": "resource not found"
                    }), 404
"""

"""
STATUS: DONE
@TODO: implement error handler for 404
    error handler should conform to general task above
"""


@app.errorhandler(404)
def not_found(error):
    return (
        jsonify(
            {"success": False, "error": 404, "message": "resource not found"}
        ),
        404,
    )


@app.errorhandler(422)
def unprocessable(error):
    return (
        jsonify({"success": False, "error": 422, "message": "unprocessable"}),
        422,
    )


"""
STATUS: DONE
@TODO: implement error handler for AuthError
    error handler should conform to general task above
"""


@app.errorhandler(AuthError)
def handle_auth_error(error):
    """
    List of errors:
        - 400: invalid_header
            Unable to parse authentication token
        - 400: invalid_token
            Token format is invalid
        - 401: invalid_claims
            Incorrect claims. Please, check the audience and issuer
        - 401: token_expired
            Token expired
        - 403: "unauthorized"
            Permission not granted
    """
    return jsonify(error.error), error.status_code


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=True)
