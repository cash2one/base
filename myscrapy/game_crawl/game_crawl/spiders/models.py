
from sqlalchemy import *
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

#ENGINE    = create_engine('postgresql://localhost/onesplay')
#ENGINE    = create_engine('postgresql://user:password@106.186.126.90/leyotv')
ENGINE    = create_engine('postgresql://user:password@localhost/leyotv')
#engine    = create_engine("mysql+pymysql://root:920214@127.0.0.1:3306/OnesPlay")
#db_connection     = ENGINE.connect()

#from sqlalchemy.orm import sessionmaker
# DB_Session = sessionmaker(bind=ENGINE)
# session    = DB_Session()

BaseModel = declarative_base()

def init_db():
    BaseModel.metadata.create_all(ENGINE)

def drop_db():
    BaseModel.metadata.drop_all(ENGINE)

class Game(BaseModel):
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    package_name = Column(String(128) , index=True, nullable=False)
    apk_mesg = Column(Text)
    game_pic = Column(String(255))
    game_type = Column(Integer, default=1) 
    view_count = Column(Integer, default=0)
    rate = Column(Float, default=10)
    show = Column(Boolean, default=True)
    ios_url = Column(String(255))
    android_url = Column(String(255))
    description = Column(Text)
    date_update = Column(DateTime, default=datetime.now, onupdate=datetime.now)

import redis

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

#WAIT_SET = "wait_set"
DONE_SET = "done_set"

game_table = Game.__table__
