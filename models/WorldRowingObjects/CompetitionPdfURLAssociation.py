from sqlalchemy import *
from ..Base import Base

CompetitionPdfURLAssociation = Table('CompetitionPdfURLAssociation', Base.metadata,
    Column('PdfURLId', String(255), ForeignKey('PdfURL.id')),
    Column('CompetitionId', String(255), ForeignKey('Competition.id'))
)