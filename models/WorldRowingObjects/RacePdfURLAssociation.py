from sqlalchemy import *
from ..Base import Base

RacePdfURLAssociation = Table('RacePdfURLAssociation', Base.metadata,
    Column('RaceId', String(255), ForeignKey('Race.id')),
    Column('PdfURLId', String(255), ForeignKey('PdfURL.id'))
)