#!/usr/bin/python3
"""python file that contains the class definition of a State"""
from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class State(Base):
    """states table"""
    __tablename__ = "states"
    id = Column("id", Integer, primary_key=True, unique=True,
                nullable=False, autoincrement=True)
    name = Column("name", String(128), nullable=False)
    cities = relationship("City",cascade='all, delete', backref='state')

 