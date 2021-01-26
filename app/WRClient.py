import sys
sys.path.append('..')

import json
import requests
from dateutil.parser import parse
from datetime import datetime
import re
import time
import urllib.request
import os
import traceback
import sys

from app.WRDecoder import WRDecoder


def gen_dict_extract(key, var):
	# if hasattr(var,'items'):
	for k, v in var.items():
		if k == key:
			yield v
		if isinstance(v, dict):
			for result in gen_dict_extract(key, v):
				yield result
		elif isinstance(v, list):
			for d in v:
				for result in gen_dict_extract(key, d):
					yield result

def cleanupData(listOfDicts):
	# takes in list of dict objects created from json, then removes metadata and modifies id attribute to distinguish some classes (BoatClass/Gender/PersonType)
	# returns as string to take advantage of object_hook
	replacements = {
		'gender': 'genderId',
		'personTypes': 'personTypeId',
		'boatClass': 'boatClassId',
		'racePhase': 'racePhaseId',
		'raceStatus': 'raceStatusId'
	}
	if 'data' in listOfDicts:
		for baseObject in listOfDicts['data']:
			for k, v in replacements.items():
				for fixObject in gen_dict_extract(k, baseObject):				
					if isinstance(fixObject, list):
						for fixListObject in fixObject:
							fixListObject[v] = fixListObject['id']
							del fixListObject['id']
					else:
						fixObject[v] = fixObject['id']
						del fixObject['id']
	else:
		print("Could not find data when getting from api?")
		print(listOfDicts)
		sys.exit()
		
	return json.dumps(listOfDicts['data'])


def getURL(endpoint, filters=[], includes=[]):
	baseURL = 'https://world-rowing-api.soticcloud.net/stats/api/' + endpoint
	# print("Filters:")
	# print(filters)

	if len(filters) + len(includes) > 0:
		baseURL = baseURL + '?'

		for currFilter in filters:
			baseURL = baseURL + 'filter[' + currFilter['object'] + ']=' + currFilter['target'] + '&'

		if len(includes) > 0:
			baseURL = baseURL + 'include='
			for currInclude in includes:
				baseURL = baseURL + currInclude + ','

		baseURL = baseURL[:-1]

	return baseURL

def getData(endpoint, filters=[], includes=[]):
	url = getURL(endpoint, filters, includes)
	return(json.loads(requests.get(url).content)['data'])

def getMapped(target, filters=[], includes=[]):
	url = getURL(target, filters=filters, includes=includes)
	response = requests.get(url).content
	# print(response)
	print(url)
	# sys.exit()
	try:
		allData = json.loads(response)
	except:
		print(response)
		print("error: " + traceback.format_exc())
		sys.exit()

	
	# allObjects = json.loads(json.dumps(allData), object_hook=class_mapper)
	allObjects = json.loads(cleanupData(allData), cls=WRDecoder)
	return allObjects