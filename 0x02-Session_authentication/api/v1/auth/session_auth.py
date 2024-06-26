#!/usr/bin/env python3
""" 6. Basic auth
"""
from api.v1.auth.auth import Auth
from models.user import User
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

    # _________________________________________________________________________

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Returns a User ID based on a Session ID
        """
        if not session_id or not isinstance(session_id, str):
            return None

        return SessionAuth.user_id_by_session_id.get(session_id)

    # _________________________________________________________________________

    def current_user(self, request=None):
        """ Returns a User instance based on a cookie value
        """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)

        return User.get(user_id)

    # _________________________________________________________________________

    def destroy_session(self, request=None):
        """deletes the user session / logout"""
        if not request:
            return False
        sessionID = self.session_cookie(request)
        if not sessionID or not self.user_id_for_session_id(sessionID):
            return False
        self.user_id_by_session_id.pop(sessionID)
        return True
