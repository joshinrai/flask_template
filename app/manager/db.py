from sqlalchemy import create_engine, exc
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.pool import NullPool
from flask import current_app

engine = create_engine(current_app.config['SQLALCHEMY_DATABASE_URI'], poolclass=NullPool, echo=False, pool_pre_ping=True)
SessionType = scoped_session(sessionmaker(bind=engine))
Conn = engine.connect()

def mysqlconn():
    try:
        engine.connect().execute('select now()')
    except:
        Conn = engine.connect()
    finally:
        return SessionType()