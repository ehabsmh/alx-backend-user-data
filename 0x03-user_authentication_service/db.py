#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import Base, User


class DB:
    """DB class
    """
    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    # ___________________________________________________________________

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    # ___________________________________________________________________

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Adds and saves a user to the database
        returns a User object
        """
        usr = User(email=email, hashed_password=hashed_password)
        self._session.add(usr)
        self._session.commit()
        return usr

    # ___________________________________________________________________

    def find_user_by(self, **kwargs) -> User:
        """ Finds the first user matches the keyword wargs
        """
        if not kwargs:
            raise InvalidRequestError
        try:
            usr = self._session.query(User).filter_by(**kwargs).first()
            if not usr:
                raise NoResultFound
        except InvalidRequestError:
            raise

        return usr

    # ___________________________________________________________________

    def update_user(self, user_id: int, **kwargs) -> None:
        """ Uses find_user_by to locate the user to update,
        then will update the user's attributes as passed in the method's
        arguments then commit changes to the database.
        If an argument that does not correspond to a user attribute is passed,
        it raises a ValueError.
        """
        usr = self.find_user_by(id=user_id)
        for k, v in kwargs.items():
            if k not in User.__table__.columns:
                raise ValueError
            setattr(usr, k, v)

        self._session.commit()
