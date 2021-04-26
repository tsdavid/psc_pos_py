import sqlite3
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
print(sqlite3.version)
print(sqlite3.sqlite_version)
print(sqlalchemy.__version__)


# LEARN FROM http://hleecaster.com/python-sqlite3/
# DB 생성 (오토 커밋)
conn = sqlite3.connect("test.db", isolation_level=None)

# 커서 획득
c = conn.cursor()

# 테이블 생성 (데이터 타입은 TEST, NUMERIC,INTEGER, REAL, BLOB 등)
c.execute("CREATE TABLE IF NOT EXISTS table1 \
          (id integer PRIMARY KEY, name text, birthday text)")
print("Create Table With SQLITE3")


# Use ORM sqlalchemy
BASE = declarative_base()

class Note(BASE):
    __tablename__ = 'note'
    id = Column(Integer, primary_key=True)
    text = Column(String(1000), nullable=False)
    x = Column(Integer, nullable=False, default=0)
    y = Column(Integer, nullable=False, default=0)



engine = sqlalchemy.create_engine('sqlite:///test.db')
BASE.metadata.create_all(engine)
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()


