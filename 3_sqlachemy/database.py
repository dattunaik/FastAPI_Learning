#setup database connection & foundational components of ORM
#Centralizes the DB Setup, making it reusable across the app for sessions and models 

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQL_ALCHEMY_DATABASE_URL = "sqlite:///./test.db" #making test.db in the current folder 

#establish the connection to the database
engine =create_engine(
    SQL_ALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
    #connect_args={'check_same_thread': False} -> SQLite-specific to allow connection across threads
    )

#helps to create new database sessions 
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False) 
    # autoflush=False -> SQLAlchemy will not automatically flush changes to the DB unless explicitly committed or refreshed
    # autocommit=False -> Disables automatic commit after each query 

Base = declarative_base()
# creates a base class for models to inherit from, linking the python classes with DB Tables 