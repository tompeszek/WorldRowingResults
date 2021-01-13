from sqlalchemy import *
from sqlalchemy.orm import relationship
from ..Base import Base
from sqlalchemy import ForeignKey

class Gender(Base):
	__tablename__ = 'Gender'

	id = Column(String(255), primary_key=True)
	Description = Column(String(255))
	
	# Don't know how to figure out what this object is or how to get it??

	Races = relationship("Race", back_populates="Gender")
	Persons = relationship("Person", back_populates="Gender")