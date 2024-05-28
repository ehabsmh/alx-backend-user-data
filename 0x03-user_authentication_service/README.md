<p align="center">
  <img src="https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png" />
</p>

# This project implementing a User Authentication System
**You should use `auth_venv` virtual environment as compiler to run python scripts:**

```bash
source auth_venv/bin/activate
```

## Tasks
[0. User model](https://github.com/ehabsmh/alx-backend-user-data/blob/main/0x03-user_authentication_service/user.py)
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
