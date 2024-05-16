#!/usr/bin/env python3
"""5. Encrypting passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Returns a salted, hashed password, which is a byte string."""
    byte_str = bytes(password, encoding='utf-8')
    return bcrypt.hashpw(byte_str, bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validates that the provided password matches the hashed password."""
    byte_str = bytes(password, encoding='utf-8')
    if bcrypt.checkpw(byte_str, hashed_password):
        return True

    return False
