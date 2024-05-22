#!/usr/bin/env python3
""" 6. Basic auth
"""
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """ Represents Session Authentication-Type
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a session id for authenticated user"""
        if not user_id or not isinstance(user_id, str):
            return None

        session_id = str(uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id
        return session_id
