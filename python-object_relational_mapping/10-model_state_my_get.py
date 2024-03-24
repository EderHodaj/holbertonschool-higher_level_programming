#!/usr/bin/python3
"""Prints the State object with the name passed as argument"""

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
    query = session.query(State).filter(State.name == argv[4]).first()
    if query is None:
        print("Not found")
    else:
        print(f"{query.id}")
    session.close()
