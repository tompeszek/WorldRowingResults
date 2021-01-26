from sqlalchemy import *
from sqlalchemy.orm import relationship
from ..Base import Base
from sqlalchemy import ForeignKey
from models.WorldRowingObjects.PersonTypeAssociation import PersonTypeAssociation

class Person(Base):
	__tablename__ = 'Person'

	endpoint = 'person'

	id = Column(String(255), primary_key=True)
	countryId = Column(String(255), ForeignKey('Country.id'), nullable=True)
	genderId = Column(String(255), ForeignKey('Gender.genderId'))
	OVRCode = Column(Integer)
	DisplayName = Column(String(255))
	FirstName = Column(String(255))
	LastName = Column(String(255))
	BirthDate = Column(Date)
	HeightCm = Column(Integer)
	WeightKg = Column(Integer)


	# links to multiple raceboats
	RaceBoatAthletes = relationship("RaceBoatAthlete", back_populates="Person")#, cascade="all, delete-orphan")

	# links to one person (one person can have many raceboatathletes)	
	Country = relationship("Country", back_populates="Persons")
	Gender = relationship("Gender", back_populates="Persons")
	PersonPhoto = relationship("PersonPhoto", back_populates="Person")
	PersonTypes = relationship("PersonType", secondary=PersonTypeAssociation, back_populates="Persons")

	def __init__(self, id, countryId, genderId, OVRCode, DisplayName, FirstName, LastName, BirthDate, HeightCm, WeightKg, country, gender, personPhoto, personTypes):
		self.id = id
		if countryId == '':
			self.countryId = None
		else:
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
		self.Gender = gender
		if personPhoto:
			self.PersonPhoto = [personPhoto]
		self.PersonTypes = personTypes
		super(Person, self).__init__()

	def __repr__(self):
		return "<Person(id='%s', DisplayName='%s')>" % (self.id, self.DisplayName)