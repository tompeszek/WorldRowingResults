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

	# links
	Persons = relationship("Person", back_populates="Country")
	RaceBoatAthletes = relationship("RaceBoatAthlete", back_populates="Country")