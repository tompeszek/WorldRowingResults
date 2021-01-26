from sqlalchemy import *
from sqlalchemy.orm import relationship
from ..Base import Base

class Competition(Base):
	__tablename__ = 'Competition'

	endpoint = 'competition'

	id = Column(String(255), primary_key=True)
	competitionTypeId = Column(String(255), ForeignKey('CompetitionType.id'))
	venueId = Column(String(255), ForeignKey('Venue.id'))
	CompetitionCode = Column(String(255))
	DisplayName = Column(String(255))
	Year = Column(Integer)
	StartDate = Column(Date)
	EndDate = Column(Date)
	EntryDeadlineDate = Column(Date)
	IsFisa = Column(Boolean)
	HasResults = Column(Boolean, default=None)

	def __init__(self, id, competitionTypeId, venueId, CompetitionCode, DisplayName, Year, StartDate, EndDate, EntryDeadlineDate, IsFisa, HasResults, pdfUrls, competitionType, venue):
		self.id = id
		self.competitionTypeId = competitionTypeId
		self.venueId = venueId
		self.CompetitionCode = CompetitionCode
		self.DisplayName = DisplayName
		self.Year = Year
		self.StartDate = StartDate
		self.EndDate = EndDate
		self.EntryDeadlineDate = EntryDeadlineDate
		self.IsFisa = IsFisa
		self.PdfURLs = pdfUrls
		self.CompetitionType = competitionType
		if HasResults:
			self.HasResults = HasResults
		else:
			self.HasResults = None
		self.Venue = venue
		super(Competition, self).__init__()

	# many events to one competition. back_populates refers to attribute on the parent/child class
	Events = relationship("Event", back_populates="Competition")

	# links to CompetitionType; venue
	Venue = relationship("Venue", back_populates="Competitions")

	CompetitionType = relationship("CompetitionType", back_populates="Competitions")
	PdfURLs = relationship("PdfURL", secondary="CompetitionPdfURLAssociation", back_populates="Competition")

	# def __init__(self, **kwargs):
	# 	super(Competition, self).__init__(**kwargs)

	def __repr__(self):
		return "<Competition(DisplayName='%s', Year='%s', Id='%s')>" % (self.DisplayName, self.Year, self.id)