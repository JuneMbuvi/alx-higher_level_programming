#!/usr/bin/python3
"""script that lists all State objects from the database with an a"""
from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    unique_state = (
            session.query(State)
            .filter(State.name.like('%a%'))
            .order_by(State.id)
            .all()
            )
    for state in unique_state:
        print("{}: {}".format(state.id, state.name))
    session.close()
