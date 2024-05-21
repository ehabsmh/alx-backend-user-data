#!/usr/bin/env python3
""" 6. Basic auth
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth


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
