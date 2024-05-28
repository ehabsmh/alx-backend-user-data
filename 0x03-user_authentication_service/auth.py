#!/usr/bin/env python3
"""Authentication System"""
from bcrypt import hashpw, gensalt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


def _hash_password(password: str) -> bytes:
    """ Returns a salted hash of the input password
    hashed with bcrypt.hashpw
    """
    return hashpw(password.encode(), gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    # ___________________________________________________________________

    def register_user(self, email: str, password: str) -> User:
        """ Returns a User object if the user not exists in the database
        Otherwise raise ValueError
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_pw = _hash_password(password)
            usr = self._db.add_user(email, hashed_pw)
            return usr
        except InvalidRequestError:
            raise
        else:
            raise ValueError(f"User {email} already exists")
