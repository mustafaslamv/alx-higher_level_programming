#!/usr/bin/python3
"""script that prints all City objects from the database hbtn_0e_14_usa"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_city import Base, City
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, db_name), pool_pre_ping=True)
    Session = sessionmaker(engine)
    session = Session()
    result = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id).all()
    for obj in result:
        print(f"{obj.State.name}: ({obj.City.id}) {obj.City.name}")
