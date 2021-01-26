from sqlalchemy import *
from sqlalchemy.orm import relationship
from ..Base import Base
from sqlalchemy import ForeignKey
from models.WorldRowingObjects.Race import Race

class Event(Base):
	__tablename__ = 'Event'

	endpoint = 'event'

	id = Column(String(255), primary_key=True)
	competitionId = Column(String(255), ForeignKey('Competition.id'))
	competitionTypeId = Column(String(255))
	boatClassId = Column(String(255))
	RscCode = Column(String(255))
	DisplayName = Column(String(255))
	boatClassId = Column(String(255), ForeignKey('BoatClass.boatClassId'))

	def __init__(self, id, competitionId, competitionTypeId, boatClassId, RscCode, DisplayName, boatClass):
		self.id = id
		self.competitionId = competitionId
		self.competitionTypeId = competitionTypeId
		self.boatClassId = boatClassId
		self.RscCode = RscCode
		self.DisplayName = DisplayName
		self.BoatClass = boatClass
		super(Event, self).__init__()

	# event links to one competition/class
	Competition = relationship("Competition", back_populates="Events")
	BoatClass = relationship("BoatClass", back_populates="Events")

	# event has multiple races
	Races = relationship("Race", back_populates="Event")