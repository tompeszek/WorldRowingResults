import sys
sys.path.append('..')

from lib.db import db_session, engine
from models.WorldRowingObjects.Competition import Competition
from models.WorldRowingObjects.Event import Event
from models.WorldRowingObjects.Race import Race
from models.WorldRowingObjects.RaceBoat import RaceBoat
from models.WorldRowingObjects.RaceBoatAthlete import RaceBoatAthlete
from models.WorldRowingObjects.Person import Person
from models.WorldRowingObjects.Country import Country
from models.WorldRowingObjects.RaceStatus import RaceStatus
from models.WorldRowingObjects.RacePhase import RacePhase
from models.WorldRowingObjects.Gender import Gender
from models.Base import Base
import WRClient

# Competition
## Event
### Race
#### RaceBoat
#### Country
#### Gender
#### RacePhase
#### RaceStatus
##### RaceBoatAthlete
###### Person
###### Country
###### Gender

if __name__ == '__main__':
	print("Starting...")
	Base.metadata.drop_all(engine)
	Base.metadata.create_all(engine)
	existingCompetitions = Competition.query.all()
	existingEvents = Event.query.all()

	allCompetitions = WRClient.getGeneric(Competition)
	addCompeititons = [x for x in allCompetitions if x.id not in [y.id for y in existingCompetitions]]

	allEvents = WRClient.getGeneric(Event)
	addEvents = [x for x in allEvents if x.id not in [y.id for y in existingEvents]]

	# for event in addEvents:
		

	db_session.add_all(addCompeititons)
	db_session.add_all(addEvents)
	db_session.commit()