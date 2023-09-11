#!/usr/bin/python3
"Lists all State objects from the database hbtn_0e_6_usa"
from sqlalchemy import create_engine, insert, update, delete
from model_state import Base, State
from model_city import City
from sys import argv
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(("mysql+mysqldb://{}:{}@localhost:3306/{}"
                            .format(argv[1], argv[2], argv[3])))
    Session = sessionmaker(bind=engine)
    session = Session()

    test = session.query(City, State).filter(City.state_id == State.id).all()
    for x, y in list(test):
        for j in list(y):
            print(j)