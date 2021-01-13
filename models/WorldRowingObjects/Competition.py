from sqlalchemy import *
from sqlalchemy.orm import relationship
from ..Base import Base

class Competition(Base):
	__tablename__ = 'Competition'

	endpoint = 'competition'

	id = Column(String(255), primary_key=True)
	competitionTypeId = Column(String(255))
	venueId = Column(String(255))
	CompetitionCode = Column(String(255))
	DisplayName = Column(String(255))
	Year = Column(Integer)
	StartDate = Column(Date)
	EndDate = Column(Date)
	EntryDeadlineDate = Column(Date)
	IsFisa = Column(Boolean)
	HasResults = Column(Boolean)

	# many events to one competition. back_populates refers to attribute on the parent/child class
	Events = relationship("Event", back_populates="Competition")

	# links to CompetitionType; venue

	# def __init__(self, **kwargs):
	# 	super(Competition, self).__init__(**kwargs)

	def __repr__(self):
		return "<Competition(DisplayName='%s', Year='%s')>" % (self.DisplayName, self.Year)