from sqlalchemy import *
from sqlalchemy.orm import relationship
from ..Base import Base
from sqlalchemy import ForeignKey

class RaceBoat(Base):
	__tablename__ = 'RaceBoat'

	id = Column(String(255), primary_key=True)
	boatId = Column(String(255))
	countryId = Column(String(255), ForeignKey('Country.id'))
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
	Country = relationship("Country", back_populates="RaceBoats")

	# many raceboatathletes per raceboat
	RaceBoatAthletes = relationship("RaceBoatAthlete", back_populates="RaceBoat")

	def __init__(self, id, boatId, countryId, worldBestTimeId, raceId, DisplayName, Rank, Lane, WorldCupPoints, InvalidMarkResult, Remark, ResultTime, country, raceBoatAthletes):
		self.id = id
		self.boatId = boatId
		self.countryId = countryId
		self.worldBestTimeId = worldBestTimeId
		self.raceId = raceId
		self.DisplayName = DisplayName
		self.Rank = Rank
		self.Lane = Lane
		self.WorldCupPoints = WorldCupPoints
		self.InvalidMarkResult = InvalidMarkResult
		self.Remark = Remark
		self.ResultTime = ResultTime
		self.Country = country
		self.RaceBoatAthletes = raceBoatAthletes
		super(RaceBoat, self).__init__()

	def __repr__(self):
		return "<RaceBoat(DisplayName='%s')>" % (self.DisplayName)