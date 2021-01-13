from sqlalchemy import *
from sqlalchemy.orm import relationship
from ..Base import Base
from sqlalchemy import ForeignKey

# TODO: not sure if this composite key is right

class RaceBoatAthlete(Base):
	__tablename__ = 'RaceBoatAthlete'

	raceBoatId = Column(String(255), ForeignKey('RaceBoat.id'), primary_key=True)
	personId = Column(String(255), ForeignKey('Person.id'), primary_key=True)
	countryId = Column(String(255), ForeignKey('Country.id'))
	boatPosition = Column(String(20))

	# links to one raceboat
	RaceBoat = relationship("RaceBoat", back_populates="RaceBoatAthletes")

	# links to one person (one person can have many raceboatathletes)
	Person = relationship("Person", back_populates="RaceBoatAthletes")
	Country = relationship("Country", back_populates="RaceBoatAthletes")
