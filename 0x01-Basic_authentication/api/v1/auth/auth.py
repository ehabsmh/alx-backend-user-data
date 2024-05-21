#!/usr/bin/env python3
""" 3. Auth class
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Template for all authentication system
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determines if a given path requires authentication
        Args:
            @path: The requested path.
            @excluded_path: A list of paths that do not require auth.
        """
        return False

    # _______________________________________________________________________________

    def authorization_header(self, request=None) -> str:
        """ Extracts the Authorization header from the request
        Args:
            @request: the flask request object.
        """
        return None

    # _______________________________________________________________________________

    def current_user(self, request=None) -> TypeVar('User'):
        """ Gets the current user based on the request
        Args:
            @request: the flask request object.
        """
        return None
