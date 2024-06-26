#!/usr/bin/env python3
""" 3. Auth class
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """ Template for all authentication system
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determines if a given path requires authentication.

        Args:
            @path: The requested path.
            @excluded_path: A list of paths that do not require auth.

        Returns True:

            * If no path passed.

            * If @excluded_paths is None or empty

            * If @path not in @excluded_paths

        False:

            * If @path is in @excluded_paths
        """
        if not excluded_paths or not path:
            return True

        path_with_slash = path
        if path[-1] != '/':
            path_with_slash += '/'

        if path in excluded_paths or path_with_slash in excluded_paths:
            return False

        return True

    # _______________________________________________________________________________

    def authorization_header(self, request=None) -> str:
        """ Extracts the Authorization header from the request

        Args:
            @request: the flask request object.
        """
        if not request:
            return None

        return request.headers.get('Authorization')

    # _______________________________________________________________________________

    def current_user(self, request=None) -> TypeVar('User'):
        """ Gets the current user based on the request
        Args:
            @request: the flask request object.
        """
        return None

    # _______________________________________________________________________________

    def session_cookie(self, request=None):
        """ Returns a cookie value from a request
        """
        if not request:
            return None

        SESSION_NAME = getenv('SESSION_NAME')
        return request.cookies.get(SESSION_NAME)
