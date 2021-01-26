from sqlalchemy import *
from sqlalchemy.orm import relationship
from ..Base import Base
from sqlalchemy import ForeignKey

class RacePhase(Base):
	__tablename__ = 'RacePhase'

	racePhaseId = Column(String(255), primary_key=True)
	DisplayName = Column(String(255))
	
	# Don't know how to figure out what this object is or how to get it??

	Races = relationship("Race", back_populates="RacePhase")

	def __init__(self, racePhaseId, DisplayName):
		self.racePhaseId = racePhaseId
		self.DisplayName = DisplayName
		super(RacePhase, self).__init__()