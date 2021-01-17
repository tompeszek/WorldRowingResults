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
import json
import requests

####### Rough hierarcy of world rowing objects with example #######

# Competition (2017 World Championships)
## Event (Men's Eight)
### Race (FA)
#### Country (USA)
#### Gender (Male)
#### RacePhase (Final)
#### RaceStatus (Completed)
#### RaceBoat (USA's entry)
##### Country (USA)
##### RaceBoatAthlete (Tom Peszek in USA Eight)
###### Person (Tom Peszek)
####### Country (USA)
####### Gender (Male)

getEventsAndComps = True

def class_mapper(d):
    for keys, cls in mapping.items():
        if keys.issuperset(d.keys()):
            return cls(**d)
    else:
        # Raise exception instead of silently returning None
        raise ValueError('Unable to find a matching class for object: {!s}'.format(d))

def setupDefaults(db_session):
	racePhases = [
		RacePhase('0959f5e8-f85a-40fb-93ab-b6c477f6aade', 'Repechage'),
		RacePhase('e0fc3320-cd66-43af-a5b5-97afd55b2971', 'Final'),
		RacePhase('e6693585-d2cf-464c-9f8e-b2e531b26400', 'Semifinal'),
		RacePhase('cd3d5ca1-5aed-4146-b39b-a192ae6533f1', 'Heat')
	]
	
	raceStatuses = [
		RaceStatus('182f6f15-8e78-41c3-95b3-8b006af2c6a1', 'Complete')
	]

	genders = [
		Gender('95b62e87-cd87-4df4-b566-6f3a64e4d366', 'Male'),
		Gender('5beae5a3-10e4-4d33-96e5-c1a9f612dd54', 'Female')
	]

	db_session.add_all(racePhases + raceStatuses + genders)
	db_session.commit()

if __name__ == '__main__':
	
	if getEventsAndComps:

		# recreate database
		Base.metadata.drop_all(engine)
		Base.metadata.create_all(engine)

		# not sure how to get phases/statuses/genders from api, so creating these manually
		setupDefaults(db_session)

		# api makes it easy to get all competitions and all events, so we do that here
		existingCompetitions = Competition.query.all()
		existingEvents = Event.query.all()

		allCompetitions = WRClient.getGeneric(Competition)
		addCompeititons = [x for x in allCompetitions if x.id not in [y.id for y in existingCompetitions]]

		allEvents = WRClient.getGeneric(Event)
		addEvents = [x for x in allEvents if x.id not in [y.id for y in existingEvents]]

		# commit events/competitions that we don't already have in database
		db_session.add_all(addCompeititons)
		db_session.add_all(addEvents)
		db_session.commit()

	# get all events in database
	existingEvents = Event.query.all()

	# set mapping so that json.loads can create objects. mapping determines which object based on keys that appear in json
	mapping = {
		frozenset(('id', 'competitionId', 'competitionTypeId', 'boatClassId', 'RscCode', 'DisplayName')): Event,
		frozenset(('id', 'eventId', 'racePhaseId', 'raceStatusId', 'genderId', 'RscCode', 'DisplayName', 'RaceNr', 'IsStarted', 'Date', 'DateString', 'Progression', 'raceBoats')): Race,
		frozenset(('id', 'boatId', 'countryId', 'worldBestTimeId', 'raceId', 'DisplayName', 'Rank', 'Lane', 'WorldCupPoints', 'InvalidMarkResult', 'Remark', 'ResultTime', 'country', 'raceBoatAthletes')): RaceBoat,
		frozenset(('id', 'Description')): RaceStatus,		
		frozenset(('raceBoatId', 'personId', 'boatPosition', 'person')): RaceBoatAthlete,
		frozenset(('id', 'countryId', 'genderId', 'OVRCode', 'DisplayName', 'FirstName', 'LastName', 'BirthDate', 'HeightCm', 'WeightKg', 'country')): Person,
		frozenset(('id', 'DisplayName', 'CountryCode', 'IsNOC', 'IsFormerCountry')): Country,		
		frozenset(('id', 'Description')): Gender
	}

	# for each event, get full results and save to database
	for event in existingEvents:
		filters = [
			{'object': 'event.id', 'target': event.id}
		]
		includes = [
			'racePhase', 'raceBoats.raceBoatAthletes.person', 'raceBoats.raceBoatAthletes.person.country,raceBoats.country'
		]
		url = WRClient.getURL(Race.endpoint, filters=filters, includes=includes)

		# i don't like this but not sure how else to use only 'data' from api response, and ignore 'meta'
		allData = json.loads(requests.get(url).content)['data']
		Races = json.loads(json.dumps(allData), object_hook=class_mapper)

		### want to do this but having trouble with foreign key constraints... like it's not uploading them all in once transaction? or maybe my models are incomplete
		print(Races)
		db_session.add_all(Races)
		db_session.commit()