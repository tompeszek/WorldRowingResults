from sqlalchemy import *
from sqlalchemy.orm import relationship
from ..Base import Base

from models.WorldRowingObjects.CompetitionTypeCompetitionCategoryAssociation import CompetitionTypeCompetitionCategoryAssociation

class CompetitionType(Base):
	__tablename__ = 'CompetitionType'

	id = Column(String(255), primary_key=True)
	DisplayName = Column(String(255))	
	Abbreviation = Column(String(255))

	def __init__(self, id, DisplayName, Abbreviation, competitionCategory):
		self.id = id
		self.DisplayName = DisplayName
		self.Abbreviation = Abbreviation
		if isinstance(competitionCategory, list):
			self.CompetitionCategory = competitionCategory
		else:
			self.CompetitionCategory = [competitionCategory]
		super(CompetitionType, self).__init__()

	Competitions = relationship("Competition", back_populates="CompetitionType")
	CompetitionCategory = relationship("CompetitionCategory", secondary=CompetitionTypeCompetitionCategoryAssociation, back_populates="CompetitionType")