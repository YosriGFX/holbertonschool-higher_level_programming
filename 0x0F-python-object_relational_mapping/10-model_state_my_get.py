#!/usr/bin/python3
'''File Doc'''
import sqlalchemy
from sys import argv
from model_state import Base, State
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
    state_name = argv[4]
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(
        State
        ).order_by(
        State.id
        ).filter(
        State.name == state_name
    ).all()
    if states:
        for state in states:
            print(state.id)
    else:
        print('Not found')
    session.close()
