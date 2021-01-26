from sqlalchemy import *
from sqlalchemy.orm import relationship
from ..Base import Base
from sqlalchemy import ForeignKey

class BoatClass(Base):
	__tablename__ = 'BoatClass'

	boatClassId = Column(String(255), primary_key=True)
	DisplayName = Column(String(255))

	def __init__(self, boatClassId, DisplayName):
		self.boatClassId = boatClassId
		self.DisplayName = DisplayName
		super(BoatClass, self).__init__()

	Events = relationship("Event", back_populates="BoatClass")


	# BoatClass links to one competition
	# Competition = relationship("Competition", back_populates="BoatClasss")

	# BoatClass has multiple races
	# Races = relationship("Race", back_populates="BoatClass")