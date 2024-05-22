#!/usr/bin/env python3
""" 6. Basic auth
"""
from flask import request
from typing import Tuple, TypeVar
from api.v1.auth.auth import Auth
from models.user import User
import base64


class BasicAuth(Auth):
    """ Represents Basic Authentication type
    """
    def extract_base64_authorization_header(self, auth_header: str) -> str:
        """ Returns the Base64 part of the
        Authorization header for a Basic Authentication
        """
        if (not auth_header
           or type(auth_header) is not str
           or not auth_header.startswith("Basic ")):
            return None

        return auth_header.split(' ')[1]

    # ___________________________________________________________________________

    def decode_base64_authorization_header(self, b64_auth_header: str) -> str:
        """ Returns the decoded value of a Base64 string @b64_auth_header"""
        if not b64_auth_header or type(b64_auth_header) is not str:
            return None

        decoded_str = ''
        try:
            decoded_str = base64.b64decode(b64_auth_header).decode('utf8')
        except Exception:
            return None
        else:
            return decoded_str

    # ___________________________________________________________________________

    def extract_user_credentials(self, decoded_b64_auth_h: str
                                 ) -> Tuple[str, str]:
        """ Returns the user email and password from the Base64 decoded value.
        """
        if not decoded_b64_auth_h or type(decoded_b64_auth_h) is not str:
            return (None, None)

        splitted_auth_header = decoded_b64_auth_h.split(':')
        if (len(splitted_auth_header) != 2):
            return (None, None)

        user_email, pw = splitted_auth_header
        return (user_email, pw)

    # ___________________________________________________________________________

    def user_object_from_credentials(self, user_email: str, user_pwd: str
                                     ) -> TypeVar('User'):
        """ Returns the User instance based on his email and password.
        """

        if not user_email or type(user_email) is not str \
           or not user_pwd or type(user_pwd) is not str:
            return None

        try:
            user = User.search({"email": user_email})
        except Exception:
            return None

        if not user:
            return None

        user = user[0]
        if not user.is_valid_password(user_pwd):
            return None

        return user

    # ___________________________________________________________________________

    def current_user(self, request=None) -> TypeVar('User'):
        """ Overloads Auth and retrieves the User instance for a request
        """
        # Get Authorization header
        auth_header = self.authorization_header(request)

        # Extract the part after Basic by extract_base64_authorization_header
        b64_part = self.extract_base64_authorization_header(auth_header)

        # decode it by decode_base64_authorization_header
        decoded_str = self.decode_base64_authorization_header(b64_part)

        # Extract the credentials by extract_user_credentials
        creds = self.extract_user_credentials(decoded_str)
        if not creds:
            return None

        # Return the user by user_object_from_credentials
        user = self.user_object_from_credentials(*creds)
        if not user:
            return None

        return user
