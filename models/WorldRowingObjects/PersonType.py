from sqlalchemy import *
from sqlalchemy.orm import relationship
from ..Base import Base
from sqlalchemy import ForeignKey
from models.WorldRowingObjects.Race import Race
from models.WorldRowingObjects.PersonTypeAssociation import PersonTypeAssociation

# many to many with Person
class PersonType(Base):
	__tablename__ = 'PersonType'

	personTypeId = Column(String(255), primary_key=True)
	DisplayName = Column(String(255))

	def __init__(self, personTypeId, DisplayName):
		self.personTypeId = personTypeId
		self.DisplayName = DisplayName
		super(PersonType, self).__init__()

	Persons = relationship("Person", secondary=PersonTypeAssociation, back_populates="PersonTypes")


	# BoatClass links to one competition
	# Competition = relationship("Competition", back_populates="BoatClasss")

	# BoatClass has multiple races
	# Races = relationship("Race", back_populates="BoatClass")


	# ValueError: Unable to find a matching class for object: {'id': 'd5169b4c-3048-49c6-8bc6-6a5c0cd1f9ba', 'countryId': '2ae87fc0-5c90-44b1-97f2-9dfdd275ab43', 
	# 'genderId': 'fbfcf4a9-23d1-42a6-b497-4ff5ed6f566d', 'OVRCode': 9512, 'DisplayName': 'SAKICKIENE, Birute', 'FirstName': 'SAKICKIENE', 'LastName': 'Birute', 
	# 'BirthDate': '1968-11-26 00:00:00', 'HeightCm': 187, 'WeightKg': 81, 
	# 'personTypes': [<models.WorldRowingObjects.BoatClass.BoatClass object at 0x00000250C9B989B0>, <models.WorldRowingObjects.BoatClass.BoatClass object at 0x00000250C9B98AC8>]}