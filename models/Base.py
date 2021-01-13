import sys
sys.path.append('..')

from sqlalchemy.ext.declarative import declarative_base
from lib.db import db_session

Base = declarative_base()
Base.query = db_session.query_property()