<p align="center">
  <img src="https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png" />
</p>

# This project implementing a User Authentication System
**You should use `auth_venv` virtual environment's python interpreter to run python scripts:**

```bash
source auth_venv/bin/activate
```

## Tasks
### [0. User model](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x03-user_authentication_service/user.py)
In this task you will create a SQLAlchemy model named `User` for a database table named `users` (by using the [mapping declaration](https://docs.sqlalchemy.org/en/13/orm/tutorial.html#declare-a-mapping) of SQLAlchemy).

The model will have the following attributes:

- `id`, the integer primary key
- `email`, a non-nullable string
- `hashed_password`, a non-nullable string
- `session_id`, a nullable string
- `reset_token`, a nullable string

test it with [0-main.py](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x03-user_authentication_service/1-main.py):

---

### [1. create user](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x03-user_authentication_service/db.py)
In this task, you will complete the `DB` class provided below to implement the `add_user` method.
```py
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session
```
Note that `DB._session` is a private property and hence should NEVER be used from outside the `DB` class.

Implement the `add_user` method, which has two required string arguments: `email` and `hashed_password`, and returns a `User` object. The method should save the user to the database. No validations are required at this stage.

test it with [1-main.py](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x03-user_authentication_service/1-main.py):

---

### [2. Find user](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x03-user_authentication_service/db.py)
In this task you will implement the `DB.find_user_by` method. This method takes in arbitrary keyword arguments and returns the first row found in the `users` table as filtered by the method’s input arguments. No validation of input arguments required at this point.

Make sure that SQLAlchemy’s `NoResultFound` and `InvalidRequestError` are raised when no results are found, or when wrong query arguments are passed, respectively.

Warning:

- `NoResultFound` has been moved from `sqlalchemy.orm.exc` to `sqlalchemy.exc` between the version 1.3.x and 1.4.x of SQLAchemy - please make sure you are importing it from `sqlalchemy.orm.exc`

---

### [3. update user](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x03-user_authentication_service/db.py)
n this task, you will implement the `DB.update_user` method that takes as argument a required `user_id` integer and arbitrary keyword arguments, and returns `None`.

The method will use `find_user_by` to locate the user to update, then will update the user’s attributes as passed in the method’s arguments then commit changes to the database.

If an argument that does not correspond to a user attribute is passed, raise a `ValueError`.

---

### [4. Hash password](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x03-user_authentication_service/auth.py)
In this task you will define a `_hash_password` method that takes in a `password` string arguments and returns bytes.

The returned bytes is a salted hash of the input password, hashed with `bcrypt.hashpw`.

---

### [5. Register user](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x03-user_authentication_service/auth.py)
In this task, you will implement the `Auth.register_user` in the `Auth` class provided below:
```py
from db import DB


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()
```
Note that `Auth._db` is a private property and should NEVER be used from outside the class.

`Auth.register_user` should take mandatory `email` and `password` string arguments and return a `User` object.

If a user already exist with the passed email, raise a `ValueError` with the message U`ser <user's email> already exists`.

If not, hash the password with `_hash_password`, save the user to the database using `self._db` and return the `User` object.

---

### [6. Basic Flask app](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x03-user_authentication_service/app.py)
In this task, you will set up a basic Flask app.

Create a Flask app that has a single `GET` route (`"/"`) and use `flask.jsonify` to return a JSON payload of the form:

`{"message": "Bienvenue"}`
Add the following code at the end of the module:
```py
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
```

---

### [7. Register user](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x03-user_authentication_service/app.py)
In this task, you will implement the end-point to register a user. Define a `users` function that implements the `POST /users` route.

Import the `Auth` object and instantiate it at the root of the module as such:

```py
from auth import Auth


AUTH = Auth()
```
The end-point should expect two form data fields: `"email"` and `"password"`. If the user does not exist, the end-point should register it and respond with the following JSON payload:

`{"email": "<registered email>", "message": "user created"}`
If the user is already registered, catch the exception and return a JSON payload of the form

`{"message": "email already registered"}`
and return a 400 status code

Remember that you should only use `AUTH` in this app. `DB` is a lower abstraction that is proxied by `Auth`.

---

### [8. Credentials validation](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x03-user_authentication_service/auth.py)
In this task, you will implement the `Auth.valid_login` method. It should expect `email` and `password` required arguments and return a boolean.

Try locating the user by email. If it exists, check the password with `bcrypt.checkpw`. If it matches return `True`. In any other case, return `False`.

---

### [9. Generate UUIDs](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x03-user_authentication_service/auth.py)
In this task you will implement a `_generate_uuid` function in the `auth` module. The function should return a string representation of a new UUID. Use the `uuid` module.

Note that the method is private to the `auth` module and should NOT be used outside of it.

---

### [10. Get session ID](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x03-user_authentication_service/auth.py)
In this task, you will implement the `Auth.create_session` method. It takes an `email` string argument and returns the session ID as a string.

The method should find the user corresponding to the email, generate a new UUID and store it in the database as the user's `session_id`, then return the session ID.

Remember that only public methods of `self._db` can be used.

---

### [11. Log in](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x03-user_authentication_service/auth.py)
In this task, you will implement a `login` function to respond to the `POST /sessions` route.

The request is expected to contain form data with `"email"` and a `"password"` fields.

If the login information is incorrect, use `flask.abort` to respond with a 401 HTTP status.

Otherwise, create a new session for the user, store it the session ID as a cookie with key `"session_id"` on the response and return a JSON payload of the form
`{"email": "<user email>", "message": "logged in"}`

**Run this command to register:**

`curl -XPOST localhost:5000/users -d 'email=bob@bob.com' -d 'password=mySuperPwd'`

**Run this command to login:**

`curl -XPOST localhost:5000/sessions -d 'email=bob@bob.com' -d 'password=mySuperPwd' -v`

**Test to login with non-user:**

`curl -XPOST localhost:5000/sessions -d 'email=bob@bob.com' -d 'password=BlaBla' -v`

---

### [12. Find user by session ID](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x03-user_authentication_service/auth.py)
In this task, you will implement the `Auth.get_user_from_session_id` method. It takes a single `session_id` string argument and returns the corresponding `User` or `None`.

If the session ID is `None` or no user is found, return `None`. Otherwise return the corresponding user.

Remember to only use public methods of `self._db`.

---

### [13. Destroy session](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x03-user_authentication_service/auth.py)
In this task, you will implement `Auth.destroy_session`. The method takes a single `user_id` integer argument and returns `None`.

The method updates the corresponding user’s session ID to `None`.

Remember to only use public methods of `self._db`.

---

### [14. Log out](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x03-user_authentication_service/app.py)
In this task, you will implement a `logout` function to respond to the `DELETE /sessions` route.

The request is expected to contain the session ID as a cookie with key `"session_id"`.

Find the user with the requested session ID. If the user exists destroy the session and redirect the user to `GET /`. If the user does not exist, respond with a 403 HTTP status.

---

### [15. User profile](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x03-user_authentication_service/app.py)
In this task, you will implement a `profile` function to respond to the `GET /profile` route.

The request is expected to contain a `session_id` cookie. Use it to find the user. If the user exist, respond with a 200 HTTP status and the following JSON payload:

`{"email": "<user email>"}`

If the session ID is invalid or the user does not exist, respond with a 403 HTTP status.

---

### [16. Generate reset password token](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x03-user_authentication_service/auth.py)
In this task, you will implement the `Auth.get_reset_password_token` method. It take an `email` string argument and returns a string.

Find the user corresponding to the email. If the user does not exist, raise a `ValueError` exception. If it exists, generate a UUID and update the user's `reset_token` database field. Return the token.

---

### [17. Get reset password token](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x03-user_authentication_service/app.py)
In this task, you will implement a `get_reset_password_token` function to respond to the `POST /reset_password` route.

The request is expected to contain form data with the `"email"` field.

If the email is not registered, respond with a 403 status code. Otherwise, generate a token and respond with a 200 HTTP status and the following JSON payload:

`{"email": "<user email>", "reset_token": "<reset token>"}`

---

### [18. Update password](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x03-user_authentication_service/auth.py)
In this task, you will implement the `Auth.update_password` method. It takes `reset_token` string argument and a `password` string argument and returns `None`.

Use the `reset_token` to find the corresponding user. If it does not exist, raise a `ValueError` exception.

Otherwise, hash the password and update the user’s `hashed_password` field with the new hashed password and the `reset_token` field to `None`.

---

### [19. Update password end-point](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x03-user_authentication_service/auth.py)
In this task you will implement the `update_password` function in the `app` module to respond to the `PUT /reset_password` route.

The request is expected to contain form data with fields `"email"`, `"reset_token"` and `"new_password"`.

Update the password. If the token is invalid, catch the exception and respond with a 403 HTTP code.

If the token is valid, respond with a 200 HTTP code and the following JSON payload:


## Project Summary:
This authentication system is called Session-Based Authentication
There's a `class User` that has class attributes:

`id`: Each user should have a unique identifier so we can find a specific user easily
`email`: user email
`hashed_password`: user password should be hashed in the database to encrypt it.
`session_id`: When a user is logged in, he should be identified that he's logged in and he's authorized to access any protected page, a `session_id` defines that.
`reset_token`: Same the idea of session_id but in this case reset_token identifies a user wants to reset his password

[db.py](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x03-user_authentication_service/db.py) is the engine of the database, it is responsible to:
- Create the database.
- Create or drop tables.
- Add user.
- Update user.
- Dynamically find a user.

Here comes the power of [auth.py](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x03-user_authentication_service/auth.py) that has a full control over the database engine (db.py)


- register_user() as the name says, it is responsible to add a user to the database to register it.
- valid_login() checks if the authentication is correct (email, password), if it is correct the user should be logged in.
- create_session() it comes after the user has been logged in, as we said each authenticated user should hold a session so he can access protected routes.
- get_user_from_session_id() this method is crucial in case the user wants to access some protected resource, the server should check if he is sending the session id back or not, so if he's sending it back, we know that he still can access this protected resource.
- destroy_session() destroies the session, this is crucial when a user has been logged in, we don't want him to access the resources.
- get_reset_password_token(): when a user decides to reset the password, the first step is to give him a session for this step. This is a security step, so not anyone can reset other's passwords.
- update_password(): finally he can update his password, only if he has `reset_session`.

[app.py](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x03-user_authentication_service/app.py) defines the routes that the user accessing.
