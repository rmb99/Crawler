from sqlalchemy import Column, Integer, VARCHAR, DateTime
from sqlalchemy.orm import relationship
from . import Base


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




