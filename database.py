from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from config import database_url

def create_engine_and_session():
    engine = create_engine(database_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()