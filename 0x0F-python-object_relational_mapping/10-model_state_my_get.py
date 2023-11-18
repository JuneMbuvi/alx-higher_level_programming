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
    nametosearch = sys.argv[4]
    result = session.query(State).filter_by(name=nametosearch).first()
    if result:
        print(result.id)
    else:
        print("Not found")
    session.close()
