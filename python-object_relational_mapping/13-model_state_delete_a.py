#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter a"""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3])
    )
    Base.metadata.create_all(engine)
    session = Session(engine)
    query = session.query(State).filter(State.name.like('%a%')).all()
    if query is not None:
        for element in query:
            session.delete(element)
    session.commit()
    session.close()
