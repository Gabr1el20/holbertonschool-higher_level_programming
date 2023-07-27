#!/usr/bin/python3
"Lists all State objects from the database hbtn_0e_6_usa"
from sqlalchemy import create_engine, insert, update
from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(("mysql+mysqldb://{}:{}@localhost:3306/{}"
                            .format(argv[1], argv[2], argv[3])))
    Session = sessionmaker(bind=engine)
    session = Session()

    test = update(State).where(State.id == 2).values(name="New Mexico")
    session.execute(test)
    session.commit()
