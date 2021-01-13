from sqlalchemy import *
from sqlalchemy.orm import relationship
from ..Base import Base
from sqlalchemy import ForeignKey

class Event(Base):
	__tablename__ = 'Event'

	endpoint = 'event'

	id = Column(String(255), primary_key=True)
	competitionId = Column(String(255), ForeignKey('Competition.id'))
	competitionTypeId = Column(String(255))
	boatClassId = Column(String(255))
	RscCode = Column(String(255))
	DisplayName = Column(String(255))

	# event links to one competition
	Competition = relationship("Competition", back_populates="Events")

	# event has multiple races
	Races = relationship("Race", back_populates="Event")