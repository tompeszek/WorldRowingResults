from sqlalchemy import *
from ..Base import Base

CompetitionTypeCompetitionCategoryAssociation = Table('CompetitionTypeCompetitionCategoryAssociation', Base.metadata,
    Column('CompetitionTypeId', String(255), ForeignKey('CompetitionType.id')),
    Column('CompetitionCategoryId', String(255), ForeignKey('CompetitionCategory.id'))
)