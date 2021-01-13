from sqlalchemy import *
from sqlalchemy.orm import relationship
from ..Base import Base
from sqlalchemy import ForeignKey

class RaceBoat(Base):
	__tablename__ = 'RaceBoat'

	id = Column(String(255), primary_key=True)
	boatId = Column(String(255))
	countryId = Column(String(255))
	worldBestTimeId = Column(String(255))
	raceId = Column(String(255), ForeignKey('Race.id'))
	DisplayName = Column(String(50))
	Rank = Column(Integer)
	Lane = Column(Integer)
	WorldCupPoints = Column(Integer)
	InvalidMarkResult = Column(Boolean)
	Remark = Column(String(255))
	ResultTime = Column(Time)
	
	# raceboat links to one race
	Race = relationship("Race", back_populates="RaceBoats")

	# many raceboatathletes per raceboat
	RaceBoatAthletes = relationship("RaceBoatAthlete", back_populates="RaceBoat")