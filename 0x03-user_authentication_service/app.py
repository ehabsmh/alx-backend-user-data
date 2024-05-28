#!/usr/bin/env python3
"""6. Basic Flask app"""
from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth
from sqlalchemy.exc import InvalidRequestError

AUTH = Auth()
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/', methods=['GET'])
def index():
    """ Returns JSON payload of the form"""
    return jsonify({"message": "Bienvenue"})


# ______________________________________________________________________________


@app.route('/users', methods=['POST'])
def register():
    """Register endpoint for user authentication"""
    email = request.form.get("email")
    password = request.form.get("password")
    if not email or not password:
        abort(400)

    try:
        AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    except InvalidRequestError:
        abort(400)

    return jsonify({"email": email, "message": "user created"})


# ______________________________________________________________________________


@app.route('/sessions', methods=['POST'])
def login():
    """ Creates a new session for the user, store the session ID as a cookie
    with key "session_id" on the response.
    Returns a JSON payload of the form.
    Aborts with 401 status code if the login information is incorrect.
    """
    email = request.form.get("email")
    password = request.form.get("password")
    if not email or not password:
        abort(400)

    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)
    res = make_response(jsonify({"email": email, "message": "logged in"}))
    res.set_cookie('session_id', session_id)

    return res


# ______________________________________________________________________________


@app.route('/sessions', methods=['DELETE'])
def logout():
    """ Logging out and deletes user session for the DB
    """
    session_id = request.cookies.get('session_id')
    if not session_id:
        abort(403)

    usr = AUTH.get_user_from_session_id(session_id)
    if not usr:
        abort(403)

    AUTH.destroy_session(usr.id)

    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
