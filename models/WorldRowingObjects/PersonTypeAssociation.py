from sqlalchemy import *
from ..Base import Base

PersonTypeAssociation = Table('PersonTypeAssociation', Base.metadata,
    Column('PersonId', String(255), ForeignKey('Person.id')),
    Column('PersonTypeId', String(255), ForeignKey('PersonType.personTypeId'))
)