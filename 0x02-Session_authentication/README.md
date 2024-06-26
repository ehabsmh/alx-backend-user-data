<p align="center">
  <img src="https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png" />
</p>

# In this project, I'm learning about the authentication process and how to implement Session Authentication on a simple API.

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

### [0. Et moi et moi et moi!](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x02-Session_authentication/api/v1/app.py)
Copy all your work of the 0x06. Basic authentication project in this new folder.

In this version, you implemented a Basic authentication for giving you access to all User endpoints:

- `GET /api/v1/users`
- `POST /api/v1/users`
- `GET /api/v1/users/<user_id>`
- `PUT /api/v1/users/<user_id>`
- `DELETE /api/v1/users/<user_id>`
Now, you will add a new endpoint: `GET /users/me` to retrieve the authenticated `User` object.

- Copy folders `models` and `api` from the previous project `0x06. Basic authentication`
- Please make sure all mandatory tasks of this previous project are done at 100% because this project (and the rest of this track) will be based on it.
- Update `@app.before_request` in `api/v1/app.py`:
  - Assign the result of `auth.current_user(request)` to `request.current_user`
- Update method for the route `GET /api/v1/users/<user_id>` in `api/v1/views/users.py`:
  - If `<user_id>` is equal to me and request.current_user is `None`: `abort(404)`
  - If `<user_id>` is equal to me and request.current_user is not `None`: return the authenticated `User` in a JSON response (like a normal case of `GET /api/v1/users/<user_id>` where `<user_id>` is a valid `User` ID)
  - Otherwise, keep the same behavior

---

### [1. Empty session](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x02-Session_authentication/api/v1/app.py)
- Create a class `SessionAuth` that inherits from `Auth`. For the moment this class will be empty. It’s the first step for creating a new authentication mechanism:

  - validate if everything inherits correctly without any overloading
  - validate the “switch” by using environment variables
- Update `api/v1/app.py` for using `SessionAuth` instance for the variable `auth` depending of the value of the environment variable `AUTH_TYPE`, If `AUTH_TYPE` is equal to `session_auth`:

  - import `SessionAuth` from `api.v1.auth.session_auth`.
  - create an instance of `SessionAuth` and assign it to the variable `auth`.

Otherwise, keep the previous mechanism.

---

### [2. Create a session](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x02-Session_authentication/api/v1/auth/session_auth.py)
- Update `SessionAuth` class:

  - Create a class attribute `user_id_by_session_id` initialized by an empty dictionary
  - Create an instance method `def create_session(self, user_id: str = None) -> str:` that creates a Session ID for a `user_id`:
    - Return `None` if `user_id` is `None`
    - Return `None` if `user_id` is not a string
    - Otherwise:
      - Generate a Session ID using `uuid` module and `uuid4()` like `id` in `Base`
      - Use this Session ID as key of the dictionary `user_id_by_session_id` - the value for this key must be `user_id`
      - Return the Session ID
    - The same `user_id` can have multiple Session ID - indeed, the `user_id` is the value in the dictionary `user_id_by_session_id`

Now you an “in-memory” Session ID storing. You will be able to retrieve an `User` id based on a Session ID.

---

### [3. User ID for Session ID](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x02-Session_authentication/api/v1/auth/session_auth.py)
- Update `SessionAuth` class:

  - Create an instance method `def user_id_for_session_id(self, session_id: str = None) -> str:` that returns a `User` ID based on a Session ID:

  - Return `None` if `session_id` is `None`
  - Return `None` if `session_id` is not a string
  - Return the value (the User ID) for the key `session_id` in the dictionary `user_id_by_session_id`.
  - You must use `.get()` built-in for accessing in a dictionary a value based on key

Now you have 2 methods (`create_session` and `user_id_for_session_id`) for storing and retrieving a link between a `User` ID and a Session ID.

---

### [4. Session cookie](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x02-Session_authentication/api/v1/auth/auth.py)
Update `api/v1/auth/auth.py` by adding the method `def session_cookie(self, request=None):` that returns a cookie value from a request:

Return `None` if `request` is `None`
Return the value of the cookie named `_my_session_id` from `request` - the name of the cookie must be defined by the environment variable `SESSION_NAME`
You must use `.get()` built-in for accessing the cookie in the request cookies dictionary
You must use the environment variable `SESSION_NAME` to define the name of the cookie used for the Session ID

---

### [5. Before request](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x02-Session_authentication/api/v1/app.py)
Update the `@app.before_request` method in `api/v1/app.py`:

Add the URL path `/api/v1/auth_session/login/` in the list of excluded paths of the method `require_auth` - this route doesn’t exist yet but it should be accessible outside authentication
If `auth.authorization_header(request)` and `auth.session_cookie(request)` return `None`, `abort(401)`

---

### [6. Use Session ID for identifying a User](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x02-Session_authentication/api/v1/auth/session_auth.py)
Update `SessionAuth` class:

Create an instance method `def current_user(self, request=None):` (overload) that returns a `User` instance based on a cookie value:

- You must use `self.session_cookie(...)` and `self.user_id_for_session_id(...)` to return the User ID based on the cookie `_my_session_id`
- By using this User ID, you will be able to retrieve a `User` instance from the database - you can use `User.get(...)` for retrieving a `User` from the database.
Now, you will be able to get a User based on his session ID.
