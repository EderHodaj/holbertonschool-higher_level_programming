#!/usr/bin/python3
"""Adds the State object “Louisiana” to the database hbtn_0e_6_usa"""

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
    query = session.query(State).filter_by(id=2).first()
    if query is not None:
        query.name = "New Mexico"
        session.commit()
    session.close()
