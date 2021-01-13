from sqlalchemy import *
from sqlalchemy.orm import relationship
from ..Base import Base
from sqlalchemy import ForeignKey

class Person(Base):
	__tablename__ = 'Person'

	endpoint = 'person'

	id = Column(String(255), primary_key=True)
	countryId = Column(String(255), ForeignKey('Country.id'))
	genderId = Column(String(255), ForeignKey('Gender.id'))
	OVRCode = Column(Integer)
	DisplayName = Column(String(255))
	FirstName = Column(String(255))
	LastName = Column(String(255))
	BirthDate = Column(Date)
	HeightCm = Column(Integer)
	WeightKg = Column(Integer)

	# links to multiple raceboats
	RaceBoatAthletes = relationship("RaceBoatAthlete", back_populates="Person")

	# links to one person (one person can have many raceboatathletes)	
	Country = relationship("Country", back_populates="Persons")
	Gender = relationship("Gender", back_populates="Persons")