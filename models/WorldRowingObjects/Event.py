from sqlalchemy import *
from sqlalchemy.orm import relationship
from ..Base import Base
from sqlalchemy import ForeignKey
from models.WorldRowingObjects.Race import Race
import WRClient

class Event(Base):
	__tablename__ = 'Event'

	endpoint = 'event'

	id = Column(String(255), primary_key=True)
	competitionId = Column(String(255), ForeignKey('Competition.id'))
	competitionTypeId = Column(String(255))
	boatClassId = Column(String(255))
	RscCode = Column(String(255))
	DisplayName = Column(String(255))

	def __init__(self, id, competitionId, competitionTypeId, boatClassId, RscCode, DisplayName):
		self.id = id
		self.competitionId = competitionId
		self.competitionTypeId = competitionTypeId
		self.boatClassId = boatClassId
		self.RscCode = RscCode
		self.DisplayName = DisplayName
		super(Event, self).__init__()

	# event links to one competition
	Competition = relationship("Competition", back_populates="Events")

	# event has multiple races
	Races = relationship("Race", back_populates="Event")

	# def populateRaces(self):
	# 	filters = [
	# 		{'object': 'event.id', 'target': self.id}
	# 	]
	# 	includes = [
	# 		'racePhase', 'raceBoats.raceBoatAthletes.person'
	# 	]
	# 	data = WRClient.getData(Race.endpoint, filters=filters, includes=includes)
	# 	for race in data:

	# 	return(data)
