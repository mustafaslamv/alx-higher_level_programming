#!/usr/bin/python3
"""script that lists all State objects that contain the letter 'a'"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name = argv[4]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, db_name), pool_pre_ping=True)

    Session = sessionmaker(engine)
    session = Session()
    result = session.query(State).filter(State.name == state_name).first()
    if (result is None):
        print("Not found")
    else:
        print(result.id)
