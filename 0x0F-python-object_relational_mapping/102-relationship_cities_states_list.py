#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_100_usa"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from relationship_state import Base, State
from relationship_city import Base, City
if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(City, State).filter(
        State.cities).order_by(City.id).all()

    for obj in result:
        print(f"{obj.City.id}: {obj.City.name} -> {obj.State.name}")
