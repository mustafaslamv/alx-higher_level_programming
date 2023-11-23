#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_100_usa"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from relationship_state import Base, State
from relationship_city import Base, City

if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, db_name), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    city = City(name="San Francisco")
    new_state = State(name="California")
    new_state.cities.append(city)
    session.add(new_state)
    session.commit()
    session.close()
