#!/usr/bin/env python3
from bcrypt import hashpw, gensalt


def _hash_password(password: str):
    """ Returns a salted hash of the input password
    """
    pw_bytes = bytes(password, encoding='utf8')
    return hashpw(pw_bytes, gensalt())
