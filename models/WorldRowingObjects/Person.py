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

	def __init__(self, id, countryId, genderId, OVRCode, DisplayName, FirstName, LastName, BirthDate, HeightCm, WeightKg, country):
		self.id = id
		self.countryId = countryId
		self.genderId = genderId
		self.OVRCode = OVRCode
		self.DisplayName = DisplayName
		self.FirstName = FirstName
		self.LastName = LastName
		self.BirthDate = BirthDate
		self.HeightCm = HeightCm
		self.WeightKg = WeightKg
		self.Country = country
		super(Person, self).__init__()

	def __repr__(self):
		return "<Person(id='%s', DisplayName='%s')>" % (self.id, self.DisplayName)