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
from models.WorldRowingObjects.Venue import Venue
from models.WorldRowingObjects.PersonPhoto import PersonPhoto
from models.WorldRowingObjects.PersonType import PersonType
from models.WorldRowingObjects.CompetitionType import CompetitionType
from models.WorldRowingObjects.CompetitionCategory import CompetitionCategory
from models.WorldRowingObjects.PdfURL import PdfURL
from models.Base import Base

from models.WorldRowingObjects.PersonTypeAssociation import PersonTypeAssociation
from models.WorldRowingObjects.CompetitionTypeCompetitionCategoryAssociation import CompetitionTypeCompetitionCategoryAssociation
from models.WorldRowingObjects.CompetitionPdfURLAssociation import CompetitionPdfURLAssociation
from models.WorldRowingObjects.RacePdfURLAssociation import RacePdfURLAssociation

import WRClient
import json
import requests


### TODO:
# api endpoint: countryMedal
# from race endpoint: event.competition.competitionType.competitionCategory
# from competition endpoint: include pdfUrls,events.pdfUrls,events.races.pdfUrls,events.boatClass
# from competition endpoint: include: "competitionType,competitionType.competitionCategory,venue,venue.country",
# from person endpoint: include: "country,personGender,personPhoto,personTypes",
# from race endpoing: include=raceStatus,racePhase



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

resetDatabase = True

if __name__ == '__main__':
	print("Starting...")
	if resetDatabase:

		# recreate database
		Base.metadata.drop_all(engine)
		Base.metadata.create_all(engine)

		# get competitions
		filters = []
		includes = [
			'pdfUrls', 'competitionType', 'competitionType.competitionCategory', 'venue', 'venue.country'
		]
		allCompetitions = WRClient.getMapped(Competition.endpoint, filters, includes)

		# get events
		includes = [
			# 'pdfUrls',
			# 'races.pdfUrls',
			'boatClass' #pdfs don't seem to actually come through
		]
		allEvents = WRClient.getMapped(Event.endpoint, filters, includes)

		# commit events/competitions that we don't already have in database
		print("Merging data to database")
		for competition in allCompetitions:
			db_session.merge(competition)
			db_session.commit()
		for event in allEvents:
			db_session.merge(event)
			db_session.commit()

	# get all events in database
	existingEvents = Event.query.all()
	existingCompetitions = Competition.query.all()

	# for each competition, get full results and save to database
	## TODO: the includes list should probably be a class attribute for Race
	for competition in existingCompetitions:
		print("Adding: " + competition.DisplayName)
		filters = [
			{'object': 'event.competition.id', 'target': competition.id}
		]
		includes = [
			'gender',
			'pdfUrls',
			'racePhase',
			'raceStatus',
			'raceBoats.country',
			'raceBoats.raceBoatAthletes.person.country',
			'raceBoats.raceBoatAthletes.person.personGender',
			'raceBoats.raceBoatAthletes.person.personPhoto',
			'raceBoats.raceBoatAthletes.person.personTypes'
		]
		Races = WRClient.getMapped(Race.endpoint, filters, includes)

		# add each race in the event
		for race in [x for x in Races if x is not None]:
			try:
				db_session.merge(race)
				db_session.commit()
			except:
				print("Failed on race.id: " + race.id)
				raise