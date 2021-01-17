from sqlalchemy import *
from sqlalchemy.orm import relationship
from ..Base import Base
from sqlalchemy import ForeignKey

class RacePhase(Base):
	__tablename__ = 'RacePhase'

	id = Column(String(255), primary_key=True)
	Description = Column(String(255))
	
	# Don't know how to figure out what this object is or how to get it??

	Races = relationship("Race", back_populates="RacePhase")

	def __init__(self, id, Description):
		self.id = id
		self.Description = Description
		super(RacePhase, self).__init__()