#!/usr/bin/env python3
""" 3. Auth class
"""
from flask import request
from typing import List, TypeVar
import re


class Auth:
    """ Template for all authentication system
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determines if a given path requires authentication
        Args:
            @path: The requested path.
            @excluded_path: A list of paths that do not require auth.
        """
        if not excluded_paths or not path:
            return True

        cleaned_paths = []
        if not re.search('/$', path):
            for excluded_path in excluded_paths:
                if re.search('/$', excluded_path):
                    cleaned_path = re.sub('/$', '', excluded_path)
                    cleaned_paths.append(cleaned_path)
        else:
            cleaned_paths = excluded_paths

        if path not in cleaned_paths or not path:
            return True

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
