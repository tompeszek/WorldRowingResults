from sqlalchemy import *
from sqlalchemy.orm import relationship
from ..Base import Base
from sqlalchemy import ForeignKey

class Country(Base):
	__tablename__ = 'Country'

	endpoint = 'country'

	id = Column(String(255), primary_key=True)
	DisplayName = Column(String(255))
	CountryCode = Column(String(50))
	IsNOC = Column(Integer)
	IsFormerCountry = Column(Boolean)

	def __init__(self, id, DisplayName, CountryCode, IsNOC, IsFormerCountry):
		self.id = id
		self.DisplayName = DisplayName
		self.CountryCode = CountryCode
		self.IsNOC = IsNOC
		self.IsFormerCountry = IsFormerCountry
		super(Country, self).__init__()

	# links
	Persons = relationship("Person", back_populates="Country")
	# RaceBoatAthletes = relationship("RaceBoatAthlete", back_populates="Country")
	RaceBoats = relationship("RaceBoat", back_populates="Country")

	def __repr__(self):
		return "<Country(id='%s', DisplayName='%s')>" % (self.id, self.DisplayName)