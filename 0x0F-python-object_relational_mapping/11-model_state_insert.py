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
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name='Louisiana')
    session.add(new_state)
    state = session.query(State).filter_by(name='Louisiana').first()
    print("{}".format(state.id))
    session.commit()
    session.close()