#!/usr/bin/python3
"""first state"""
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
    Create the necessary database tables
    (if they don't exist) based on the defined models
    """
    Base.metadata.create_all(eng)

    # Create a session to interact with the database
    Session = sessionmaker(bind=eng)
    session = Session()

    # Query the state with the least ID from the 'states' table
    least_id_state = session.query(State).order_by(State.id).first()

    # Print the state ID (if a state exists)
    if least_id_state is not None:
        print("{}".format(least_id_state.id))
    else:
        print("Nothing")

    # Close the session
    session.close()

