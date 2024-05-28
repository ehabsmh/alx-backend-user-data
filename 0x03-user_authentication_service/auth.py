#!/usr/bin/env python3
"""Authentication System"""
from bcrypt import hashpw, gensalt, checkpw
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from uuid import uuid4
from typing import Union


def _hash_password(password: str) -> bytes:
    """ Returns a salted hash of the input password
    hashed with bcrypt.hashpw
    """
    return hashpw(password.encode(), gensalt())


# ________________________________________________________________________________________


def _generate_uuid() -> str:
    """ Return a string representation of a new UUID.
    """
    return str(uuid4())


# ________________________________________________________________________________________


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    # ________________________________________________________________________

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

    # ________________________________________________________________________

    def valid_login(self, email: str, password: str) -> bool:
        """Validate the user in the database
        """
        try:
            usr = self._db.find_user_by(email=email)
            if not checkpw(password.encode(), usr.hashed_password):
                raise Exception
        except Exception:
            return False
        else:
            return True

    # ________________________________________________________________________

    def create_session(self, email: str) -> str:
        """ Finds the user by email, generate a new UUID
        and store it in the database as the user's session_id.
        Returns the session ID
        """
        session_id = _generate_uuid()
        try:
            usr_id = self._db.find_user_by(email=email).id
            self._db.update_user(usr_id, session_id=session_id)
        except Exception:
            return None
        else:
            return session_id

    # ________________________________________________________________________

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """ Finds user by session ID
        Returns The corresponding User or None.
        If the session ID is None or no user is found, return None.
        Otherwise return the corresponding user.
        """
        try:
            usr = self._db.find_user_by(session_id=session_id)
            if not usr:
                return None
        except NoResultFound:
            return usr

        return usr

    # ________________________________________________________________________

    def destroy_session(self, user_id: int) -> None:
        """ Updates the corresponding user's session ID to None
        """
        self._db.update_user(user_id, session_id=None)
