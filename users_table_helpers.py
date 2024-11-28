from models import UsersModel
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text, and_
import constants as const

def populate_users_table():
    users = [
        UsersModel(name="Jenil Dave",username="davejen", password="jenil@123",admin=1),
        UsersModel(name="Riddesh Shah",username="shahrid", password="riddhesh@123",admin=0),
        UsersModel(name="Sahil Chorge",username="chorsah", password="sahil@123",admin=0),
        UsersModel(name="Kunal Maniyar",username="manikun", password="kunal@123",admin=0),
        UsersModel(name="Jash Mehta",username="mehtjas", password="jash@123",admin=0),
    ]

    with sessionmaker(bind= create_engine(const.DB_URL))() as session:
        session.execute(text('USE [Jan23TrainingDB16]'))
        for user in users:
            session.add(user)

        # Alembic starts a transaction to populate table. Thus commit is required
        session.commit()
        print("Users table population succesfull")

def read_users_table():
    with sessionmaker(bind= create_engine(const.DB_URL))() as session:
        session.execute(text('USE [Jan23TrainingDB16]'))
        users = session.query(UsersModel).all()
        for user in users:
            print(user)

        # Alembic starts a transaction to populate table. Thus commit is required
        session.commit()
        print("Users table read completed")

def read_user_by_id(id: str):
    user = None
    with sessionmaker(bind= create_engine(const.DB_URL))() as session:
        user = session.query(UsersModel).where(UsersModel.id == id)
        print(user[0].name)
    session.commit()
    return user[0].name

def auth_user_by_creds(auth_keys:dict):
    user = None
    with sessionmaker(bind= create_engine(const.DB_URL))() as session:
        user = session.query(UsersModel).where(
            and_(UsersModel.username == auth_keys['username'], UsersModel.password ==auth_keys['password']))
        print(user)
    session.commit()
    
    # if entry not found, it returns empty list
    if(user.all() != []):
        return user[0]

    # return NOT FOUND if record not found    
    return const.NOT_FOUND
