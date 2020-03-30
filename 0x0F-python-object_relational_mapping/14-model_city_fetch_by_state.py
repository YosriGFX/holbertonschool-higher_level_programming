#!/usr/bin/python3
'''File Doc'''
import sqlalchemy
from sys import argv
from model_state import Base, State
from model_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


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
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        state = session.query(State).filter(State.id == city.state_id).first()
        print(
            "{}: ({}) {}".format(
                state.name,
                city.id,
                city.name
            )
        )
    session.close()
