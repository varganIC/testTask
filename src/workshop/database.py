from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DB_USER_NAME = 'postgres'
DB_PASSWORD = 'root'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'postgres'
SQLALCHEMY_DATABASE_URL = f'postgresql://{DB_USER_NAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()







