from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgres://ksxcjfsy:TZxRyuajNQLN7k3KmUKqp6Fntc7OA0oB@elmer.db.elephantsql.com:5432/ksxcjfsy")
Session = sessionmaker(bind=engine)

Base = declarative_base()