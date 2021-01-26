from sqlalchemy import *
from sqlalchemy.orm import relationship
from ..Base import Base
from sqlalchemy import ForeignKey

# many to many with Person
class PersonPhoto(Base):
	__tablename__ = 'PersonPhoto'

	id = Column(String(255), primary_key=True)
	personId = Column(String(255), ForeignKey('Person.id'))
	url = Column(String(255))
	tags = Column(String(255))
	priority = Column(Integer)

	def __init__(self, id, personId, url, tags, priority):
		self.id = id
		self.personId = personId
		self.url = url
		self.tags = tags
		self.priority = priority
		super(PersonPhoto, self).__init__()

	Person = relationship("Person", back_populates="PersonPhoto")