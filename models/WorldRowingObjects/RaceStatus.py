from sqlalchemy import *
from sqlalchemy.orm import relationship
from ..Base import Base
from sqlalchemy import ForeignKey

class RaceStatus(Base):
	__tablename__ = 'RaceStatus'

	raceStatusId = Column(String(255), primary_key=True)
	DisplayName = Column(String(255))

	def __init__(self, raceStatusId, DisplayName):
		self.raceStatusId = raceStatusId
		self.DisplayName = DisplayName
		super(RaceStatus, self).__init__()
	
	# Don't know how to figure out what this object is or how to get it??

	Races = relationship("Race", back_populates="RaceStatus")

	def __repr__(self):
		return "<Race(DisplayName='%s')>" % (self.DisplayName)