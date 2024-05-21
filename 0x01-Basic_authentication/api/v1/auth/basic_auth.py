#!/usr/bin/env python3
""" 6. Basic auth
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
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

        decoded_bytes = ''
        try:
            decoded_bytes = base64.b64decode(b64_auth_header).decode('utf8')
        except Exception:
            return None
        else:
            return decoded_bytes
