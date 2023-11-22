#!/usr/bin/python3
"""python file that contains the class definition of a City"""
from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import declarative_base
Base = declarative_base()


class City(Base):
    """City table"""
    __tablename__ = "cities"
    id = Column("id", Integer, primary_key=True, unique=True,
                nullable=False, autoincrement=True)
    name = Column("name", String(128), nullable=False)

    state_id = Column("state_id", Integer, ForeignKey('states.id'),
                      nullable=False)
