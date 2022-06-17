from sqlalchemy import Column, Integer
from sqlalchemy import DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import MetaData

from model.config import BaseConfig

engine = create_engine(BaseConfig.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
meta = MetaData()


class Dollar(Base):
    __tablename__ = 'dollar'
    id = Column(Integer, primary_key=True)
    max_price = Column(Integer)
    min_price = Column(Integer)
    opening = Column(Integer)
    last = Column(Integer)
    percent_change = Column(Integer)
    change = Column(Integer)
    miladi_date = Column(DateTime)
    shamsi_date = Column(DateTime)


if __name__ == '__main__':
    Base.metadata.create_all(engine)