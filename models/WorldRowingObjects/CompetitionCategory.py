from sqlalchemy import *
from sqlalchemy.orm import relationship
from ..Base import Base

from models.WorldRowingObjects.CompetitionTypeCompetitionCategoryAssociation import CompetitionTypeCompetitionCategoryAssociation

class CompetitionCategory(Base):
	__tablename__ = 'CompetitionCategory'

	id = Column(String(255), primary_key=True)
	DisplayName = Column(String(255))
	CategoryType = Column(String(255))

	def __init__(self, id, DisplayName, CategoryType):
		self.id = id
		self.DisplayName = DisplayName
		if (CategoryType):
			self.CategoryType = CategoryType
		else:
			self.CategoryType = "None"
		super(CompetitionCategory, self).__init__()

	CompetitionType = relationship("CompetitionType", secondary=CompetitionTypeCompetitionCategoryAssociation, back_populates="CompetitionCategory")