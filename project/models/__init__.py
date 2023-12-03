from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()


class Base:
    # the table's primary key
    id = Column(Integer, primary_key=True, autoincrement=True)

    # the user who created the record
    created_by = Column(Integer, nullable=True)
    # the date the record was created
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    # the user who updated the record
    updated_by = Column(Integer, ForeignKey('user.id'), nullable=True)
    # the date the record was updated
    updated_at = Column(DateTime, default=datetime.utcnow)


class User(Base, DeclarativeBase):
    # the table name in the database
    __tablename__ = 'user'

    name = Column(String, nullable=False)

    address_id = Column(Integer, ForeignKey('address.id'), nullable=True)


class Address(Base, DeclarativeBase):
    __tablename__ = 'address'

    lat = Column(String, nullable=True)
    lng = Column(String, nullable=True)
    street = Column(String, nullable=True)
    neighborhood = Column(String, nullable=True)
    city = Column(String, nullable=True)
    state = Column(String, nullable=True)
    number = Column(Integer, nullable=True)
    postal_code = Column(String, nullable=True)
    additional = Column(String, nullable=True)
