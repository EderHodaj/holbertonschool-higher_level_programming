#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa."""

from sys import argv
from sqlalchemy import create_engine
from model_city import Base, City
from model_state import State
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3])
    )
    Base.metadata.create_all(engine)
    session = Session(engine)
    query = session.query(City, State).filter(City.state_id == State.id).all()
    if query is not None:
        for city, state in query:
            print(f"{state.name}: ({city.id}) {city.name}")
    session.commit()
    session.close()
