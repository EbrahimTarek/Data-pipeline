from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base

engine = create_engine("postgresql+psycopg2://postgres:0129534150Ee#@localhost:5432/newdb")
session = Session(engine)
Base = declarative_base()







