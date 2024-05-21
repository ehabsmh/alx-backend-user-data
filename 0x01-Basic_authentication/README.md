<p align="center">
  <img src="https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png" />
</p>

# In this project, I'm learning about the authentication process and how to implement Basic Authentication on a simple API.

# Simple API

Simple HTTP API for playing with `User` model.


## Files

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints


## Setup

```
$ pip3 install -r requirements.txt
```


## Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```


## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)


## Tasks

### [0. Simple-basic-API](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x01-Basic_authentication/)
Download and start your project from this archive.zip

In this archive, you will find a simple API with one model: User. Storage of these users is done via a serialization/deserialization in files.

---

### [1. Error handler: Unauthorized](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x01-Basic_authentication/app.py)

What the HTTP status code for a request unauthorized? `401` of course!

Edit `api/v1/app.py`:

Add a new error handler for this status code, the response must be:
a JSON: `{"error": "Unauthorized"}`
status code `401`
you must use `jsonify` from `Flask`
For testing this new error handler, add a new endpoint in `api/v1/views/index.py`:

Route: `GET /api/v1/unauthorized`
This endpoint must raise a 401 error by using `abort`.
By calling `abort(401)`, the error handler for 401 will be executed.

---

### [2. Error handler: Forbidden](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x01-Basic_authentication/app.py)

What the HTTP status code for a request where the user is authenticate but not allowed to access to a resource? `403` of course!

Edit `api/v1/app.py`:

Add a new error handler for this status code, the response must be:
a JSON: `{"error": "Forbidden"}`
status code `403`
you must use `jsonify` from `Flask`
For testing this new error handler, add a new endpoint in `api/v1/views/index.py`:

Route: `GET /api/v1/forbidden`
This endpoint must raise a 403 error by using `abort` - Custom Error Pages
By calling `abort(403)`, the error handler for 403 will be executed.

---

### [3. Auth class](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x01-Basic_authentication/api/v1/auth)

Now you will create a class to manage the API authentication.

- Create a folder `api/v1/auth`
- Create an empty file `api/v1/auth/__init__.py`
- Create the class `Auth`:
    - in the file `api/v1/auth/auth.py`
    - import `request` from `flask`
    - class name `Auth`
    - public method `def require_auth(self, path: str, excluded_paths: List[str]) -> bool:` that returns `False` - `path` and `excluded_paths` will be used later, now, you don’t need to take care of them.
    - public method `def authorization_header(self, request=None) -> str:` that returns `None` - `request` will be the Flask request object.
    - public method `def current_user(self, request=None) -> TypeVar('User'):` that returns `None` - `request` will be the Flask request object

This class is the template for all authentication system you will implement.
