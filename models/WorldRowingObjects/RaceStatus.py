from sqlalchemy import *
from sqlalchemy.orm import relationship
from ..Base import Base
from sqlalchemy import ForeignKey

class RaceStatus(Base):
	__tablename__ = 'RaceStatus'

	id = Column(String(255), primary_key=True)
	Description = Column(String(255))

	def __init__(self, id, Description):
		self.id = id
		self.Description = Description
		super(RaceStatus, self).__init__()
	
	# Don't know how to figure out what this object is or how to get it??

	Races = relationship("Race", back_populates="RaceStatus")

	def __repr__(self):
		return "<Race(Description='%s')>" % (self.Description)