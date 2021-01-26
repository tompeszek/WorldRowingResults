from sqlalchemy import *
from sqlalchemy.orm import relationship
from ..Base import Base
from sqlalchemy import ForeignKey
from models.WorldRowingObjects.Race import Race
from models.WorldRowingObjects.PersonTypeAssociation import PersonTypeAssociation

class PdfURL(Base):
	__tablename__ = 'PdfURL'

	id = Column(String(255), primary_key=True)
	entityId = Column(String(255))
	entityType = Column(String(255))
	orisCodeId = Column(String(255))
	DisplayName = Column(String(255))
	title = Column(String(255))
	url = Column(String(255))

	def __init__(self, id, entityId, entityType, orisCodeId, DisplayName, title, url):
		self.id = id
		self.entityId = entityId
		self.entityType = entityType
		self.orisCodeId = orisCodeId
		self.DisplayName = DisplayName
		self.title = title
		self.url = url
		super(PdfURL, self).__init__()

	Competition = relationship("Competition", secondary="CompetitionPdfURLAssociation", back_populates="PdfURLs")
	Race = relationship("Race", secondary="RacePdfURLAssociation", back_populates="PdfURLs")