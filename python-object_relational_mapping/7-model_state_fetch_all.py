#!/usr/bin/python3
"""all states via sqlalchelmy"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    # Create a database engine using the provided credentials
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))

    """
    Create the database tables
    (if they don't exist) based on the defined models
    """
    Base.metadata.create_all(eng)

    # Create a session to interact with the database
    Session = sessionmaker(bind=eng)
    session = Session()

    # Query all states from the 'states' table and order them by ID
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
