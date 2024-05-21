#!/usr/bin/env python3
""" 6. Basic auth
"""
from flask import request
from typing import List, TypeVar
from auth import Auth


class BasicAuth(Auth):
    """ Represents Basic Authentication type
    """
    pass
