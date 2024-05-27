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

    def find_user_by(self, **kwargs):
        """ Finds the first user matches the keyword wargs
        """
        try:
            usr = self._session.query(User).filter_by(**kwargs).first()
            if not usr:
                raise NoResultFound()
        except InvalidRequestError:
            raise

        return usr
