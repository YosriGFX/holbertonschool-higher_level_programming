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
    states = session.query(State).all()
    for state in states:
        print(
            "{}: {}".format(
                state.id,
                state.name
            )
        )
        for city in state.cities:
            print(
                "\t{}: {}".format(
                    city.id,
                    city.name
                )
            )
    session.close()
