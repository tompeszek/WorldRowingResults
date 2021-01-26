from sqlalchemy import *
from sqlalchemy.orm import relationship
from ..Base import Base
from sqlalchemy import ForeignKey

class Venue(Base):
	__tablename__ = 'Venue'

	endpoint = 'venue'

	id = Column(String(255), primary_key=True)
	countryId = Column(String(255), ForeignKey('Country.id'))
	DisplayName = Column(String(255))
	RegionCity = Column(String(255))
	Site = Column(String(255))
	IsWorldRowingVenue = Column(Boolean)

	def __init__(self, id, countryId, DisplayName, RegionCity, Site, IsWorldRowingVenue, country):
		self.id = id
		self.countryId = countryId
		self.DisplayName = DisplayName
		self.RegionCity = RegionCity
		self.Site = Site
		self.IsWorldRowingVenue = IsWorldRowingVenue
		self.Country = country
		super(Venue, self).__init__()

	# links
	Country = relationship("Country", back_populates="Venues")
	Competitions = relationship("Competition", back_populates="Venue")

	def __repr__(self):
		return "<Venue(id='%s', DisplayName='%s')>" % (self.id, self.DisplayName)