import json
import traceback
import sys

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
from models.WorldRowingObjects.BoatClass import BoatClass
from models.WorldRowingObjects.PersonPhoto import PersonPhoto
from models.WorldRowingObjects.PersonType import PersonType
from models.WorldRowingObjects.CompetitionType import CompetitionType
from models.WorldRowingObjects.CompetitionCategory import CompetitionCategory
from models.WorldRowingObjects.PdfURL import PdfURL

from models.WorldRowingObjects.PersonTypeAssociation import PersonTypeAssociation
from models.WorldRowingObjects.CompetitionTypeCompetitionCategoryAssociation import CompetitionTypeCompetitionCategoryAssociation
from models.WorldRowingObjects.CompetitionPdfURLAssociation import CompetitionPdfURLAssociation
from models.WorldRowingObjects.RacePdfURLAssociation import RacePdfURLAssociation

class WRDecoder(json.JSONDecoder):
	def __init__(self, *args, **kwargs):
		# TODO: the mapping here is a bit of a mess, probably get get class attributes dynmically from each class
		json.JSONDecoder.__init__(self, object_hook=self.class_mapper, *args, **kwargs)
		self.mapping = {	
			frozenset(('boatClassId', 'DisplayName')): BoatClass,
			frozenset(('genderId', 'DisplayName')): Gender,
			frozenset(('personTypeId', 'DisplayName')): PersonType,
			frozenset(('racePhaseId', 'DisplayName')): RacePhase,
			frozenset(('raceStatusId', 'DisplayName')): RaceStatus,
			frozenset(('id', 'DisplayName', 'CategoryType')): CompetitionCategory,
			frozenset(('id', 'entityId', 'entityType', 'orisCodeId', 'DisplayName', 'title', 'url')): PdfURL,
			frozenset(('id', 'DisplayName', 'Abbreviation', 'competitionCategory')): CompetitionType,
			frozenset(('id', 'competitionTypeId', 'venueId', 'CompetitionCode', 'DisplayName', 'Year', 'StartDate', 'EndDate', 'EntryDeadlineDate', 'IsFisa', 'HasResults', 'pdfUrls', 'competitionType', 'venue')): Competition,
			frozenset(('id', 'competitionId', 'competitionTypeId', 'boatClassId', 'RscCode', 'DisplayName')): Event,
			frozenset(('id', 'competitionId', 'competitionTypeId', 'boatClassId', 'RscCode', 'DisplayName', 'boatClass')): Event,
			frozenset(('id', 'eventId', 'racePhaseId', 'raceStatusId', 'genderId', 'RscCode', 'DisplayName', 'RaceNr', 'IsStarted', 'Date', 'DateString', 'Progression', 'racePhase', 'raceStatus', 'raceBoats', 'pdfUrls', 'gender')): Race,
			frozenset(('id', 'boatId', 'countryId', 'worldBestTimeId', 'raceId', 'DisplayName', 'Rank', 'Lane', 'WorldCupPoints', 'InvalidMarkResult', 'Remark', 'ResultTime', 'country', 'raceBoatAthletes')): RaceBoat,
			frozenset(('raceBoatId', 'personId', 'boatPosition', 'person')): RaceBoatAthlete,
			frozenset(('id', 'countryId', 'genderId', 'OVRCode', 'DisplayName', 'FirstName', 'LastName', 'BirthDate', 'HeightCm', 'WeightKg', 'country', 'gender', 'personPhoto', 'personTypes')): Person,
			frozenset(('id', 'countryId', 'genderId', 'OVRCode', 'DisplayName', 'FirstName', 'LastName', 'BirthDate', 'HeightCm', 'WeightKg', 'country', 'personTypes')): Person,
			frozenset(('id', 'DisplayName', 'CountryCode', 'IsNOC', 'IsFormerCountry')): Country,
			frozenset(('id', 'countryId', 'DisplayName', 'RegionCity', 'Site', 'IsWorldRowingVenue')): Venue,
			frozenset(('id', 'countryId', 'DisplayName', 'RegionCity', 'Site', 'IsWorldRowingVenue', 'country')): Venue,
			frozenset(('id', 'personId', 'url', 'tags', 'priority')): PersonPhoto
		}

	# mine
	def class_mapper(self, d):
		for keys, cls in self.mapping.items():
			if keys.issuperset(d.keys()):
				try:
					return cls(**d)
				except:
					print("******")
					print(type(d))
					print(d)
					print("******")
					print(keys)
					print("******")
					print(cls)
					print("******")
					raise
		else:
			# Raise exception instead of silently returning None
			raise ValueError('Unable to find a matching class for object: {!s}'.format(d))