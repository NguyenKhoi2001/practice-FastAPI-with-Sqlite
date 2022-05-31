from logging import raiseExceptions
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from fastapi import HTTPException, status

SQLALCHEMY_DATABASE_URL = "sqlite:///./database/blogAndUsers.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False})

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# def rawQuery(raw_query):
#     query = text(raw_query)
#     try:
#         rr = engine.execute(query).fetchall()
#     except:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'query error')
#     else:
#         res = [tuple(i) for i in rr]
#         return res

def selectQuery(raw_query):
    query = text(raw_query)
    rr = engine.execute(query).fetchall()
    res = [tuple(i) for i in rr]
    return res

def insertQuery(raw_query):
    query = text(raw_query)
    engine.execute(query)

def deleteQuery(raw_query):
    query = text(raw_query)
    try:
        engine.execute(query)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'no record found to delete')

def updateQuery(raw_query):
    query = text(raw_query)
    try:
        engine.execute(query)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'no record found to update')