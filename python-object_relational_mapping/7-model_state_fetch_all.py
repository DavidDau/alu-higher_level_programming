#!/usr/bin/python3
"""Lists all states objects from the db"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states(username, password, database_name):
    # Create engine
    engine = create_engine(f'mysql://{username}:{password}@localhost:3306/{database_name}')
    
    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Query for State objects, sorted by id
    states = session.query(State).order_by(State.id).all()
    
    # Display results
    for state in states:
        print(f"{state.id}: {state.name}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    from model_state import Base  # Importing Base here as per requirement
    from model_state import State  # Importing State here as per requirement
    
    list_states(username, password, database_name)
