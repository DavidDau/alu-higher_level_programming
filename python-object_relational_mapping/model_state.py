#!/usr/bin/python3
"""ORM"""

from sqlalchemy import Column, Integer, String, create_engine
"""SQLalchemy"""
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """Class AKA table"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

# Define engine to connect to MySQL server
engine = create_engine('mysql://username:password@localhost:3306/database')


if __name__ == "__main__":
    # Create all tables in the database
    Base.metadata.create_all(engine)
