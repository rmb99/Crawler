from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


def get_session(conn_string):
    db = create_engine(conn_string)
    Session = sessionmaker(db)
    return Session()
