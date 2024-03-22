#!/usr/bin/python3
"""Script that prints all City objects from the database hbtn_0e_14_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":
    # Extract MySQL username, password, and database name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create SQLAlchemy engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query to retrieve all City objects from the database sorted by id
    cities = session.query(City).order_by(City.id).all()

    # Print results
    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))

    # Close the session
    session.close()
