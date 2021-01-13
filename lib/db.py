import json
import sys
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine

with open('../connection.json') as f:
    settings = json.load(f)
user, password, host, driver, dbname = settings['db']['user'], settings['db']['password'], settings['db']['host'], settings['db']['driver'], settings['db']['dbname']

connection_url =  f'mssql://{user}:{password}@{host}/{dbname}?driver={driver}'
engine = create_engine(connection_url)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db_session = scoped_session(Session)