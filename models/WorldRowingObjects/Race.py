from sqlalchemy import *
from sqlalchemy.orm import relationship
from ..Base import Base
from sqlalchemy import ForeignKey

class Race(Base):
	__tablename__ = 'Race'

	endpoint = 'race'

	id = Column(String(255), primary_key=True)
	eventId = Column(String(255), ForeignKey('Event.id'))
	racePhaseId = Column(String(255), ForeignKey('RacePhase.id'))
	raceStatusId = Column(String(255), ForeignKey('RaceStatus.id'))
	genderId = Column(String(255), ForeignKey('Gender.id'))
	RscCode = Column(String(255))
	DisplayName = Column(String(50))
	RaceNr = Column(String(50))
	IsStarted = Column(Boolean)
	Date = Column(Date)
	DateString = Column(String(50))
	Progression = Column(String(50))

	# many raceboats per race
	RaceBoats = relationship("RaceBoat", back_populates="Race")

	# singles
	Event = relationship("Event", back_populates="Races")

	# singles tht are just attributes
	RacePhase = relationship("RacePhase", back_populates="Races")
	RaceStatus = relationship("RaceStatus", back_populates="Races")
	Gender = relationship("Gender", back_populates="Races")