#!/usr/bin/env python3
"""6. Basic Flask app"""
from flask import Flask, jsonify, request, abort
from auth import Auth
from sqlalchemy.exc import InvalidRequestError

AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ Returns JSON payload of the form"""
    return jsonify({"message": "Bienvenue"})

# ______________________________________________________________________________

@app.route('/users', methods=['POST'], strict_slashes=False)
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

    return jsonify({{"email": email, "message": "user created"}})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
