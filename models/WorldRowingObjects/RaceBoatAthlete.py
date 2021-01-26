from sqlalchemy import *
from sqlalchemy.orm import relationship
from ..Base import Base
from sqlalchemy import ForeignKey
from models.WorldRowingObjects.Person import Person
from models.WorldRowingObjects.Country import Country
from models.WorldRowingObjects.Gender import Gender
from models.WorldRowingObjects.PersonType import PersonType
from models.WorldRowingObjects.PersonPhoto import PersonPhoto

class RaceBoatAthlete(Base):
	__tablename__ = 'RaceBoatAthlete'

	id = Column(String(255), primary_key=True)
	raceBoatId = Column(String(255), ForeignKey('RaceBoat.id'))#, primary_key=True)
	personId = Column(String(255), ForeignKey('Person.id'))#, primary_key=True)
	boatPosition = Column(String(20))#, primary_key=True)

	# links to one raceboat
	RaceBoat = relationship("RaceBoat", back_populates="RaceBoatAthletes")

	# links to one person (one person can have many raceboatathletes)
	Person = relationship("Person", back_populates="RaceBoatAthletes")

	def __init__(self, raceBoatId, personId, boatPosition, person):
		self.id = str(raceBoatId) + str(personId) + str(boatPosition)
		self.raceBoatId = raceBoatId
		if personId is None or personId == '':
			self.personId = 'None'
		else:
			self.personId = personId
		# self.countryId = countryId
		if boatPosition is None or boatPosition == '':
			self.boatPosition = 'None'
		else:
			self.boatPosition = boatPosition
		if person is None:
			# if there's no Person object, we need a placeholder in the Person table
			self.Person = Person(
					id=personId,
					countryId='',
					genderId='',
					OVRCode='',
					DisplayName='Unknown',
					FirstName='',
					LastName='',
					BirthDate='',
					HeightCm=0,
					WeightKg=0,
					country=Country('', 'Unknown', 'Unknown', 0, 0),
					gender=Gender('', 'Unknown'),
					personPhoto=PersonPhoto('', personId, '', '', 0),
					personTypes=[PersonType('', 'Unknown')]
				)
		else:
			self.Person = person
		super(RaceBoatAthlete, self).__init__()

	def __repr__(self):
		return "<RaceBoatAthlete(personId='%s', boatPosition='%s')>" % (self.personId, self.boatPosition)