#!/usr/bin/python3
'''File Doc'''
import sqlalchemy
from sys import argv
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State


if __name__ == '__main__':
    '''init by filename'''
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1],
            argv[2],
            argv[3]
        )
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name='California')
    new_state.cities = [City(name='San Francisco')]
    session.add(new_state)
    session.commit()
    session.close()
