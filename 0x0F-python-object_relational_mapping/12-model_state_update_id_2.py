#!/usr/bin/python3
"""script that changes the name of a State object """

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
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
    new_name = session.query(State).filter(State.id == 2).first()
    new_name.name = "New Mexico"
    session.commit()
