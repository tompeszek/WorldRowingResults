from sqlalchemy import *
from sqlalchemy.orm import relationship
from ..Base import Base
from sqlalchemy import ForeignKey

class Gender(Base):
	__tablename__ = 'Gender'

	genderId = Column(String(255), primary_key=True)
	DisplayName = Column(String(255))

	def __init__(self, genderId, DisplayName):#, Races, Persons):
		self.genderId = genderId
		self.DisplayName = DisplayName
		# self.Races = Races
		# self.Persons = Persons
		super(Gender, self).__init__()
	
	Races = relationship("Race", back_populates="Gender")
	Persons = relationship("Person", back_populates="Gender")