#!/usr/bin/env python3
from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> bytes:
    """ Returns a salted hash of the input password
    hashed with bcrypt.hashpw
    """
    return hashpw(password.encode(), gensalt())
