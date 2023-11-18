#!/usr/bin/python3
"""script that eletes all State objects with a name containing the letter a"""
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
    deleted = (
            session.query(State)
            .filter(State.name.like('%a%'))
            .all()
            )
    for state in deleted:
        session.delete(state)
    session.commit()
    session.close()
