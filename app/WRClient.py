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
from models.WorldRowingObjects.Competition import Competition

def getData(endpoint, filters=[], includes=[]):
	baseURL = 'https://world-rowing-api.soticcloud.net/stats/api/' + endpoint

	if len(filters) + len(includes) > 0:
		baseURL = baseURL + '?'

		for currFilter in filters:
			baseURL = baseURL + 'filter[' + currFilter['object'] + ']=' + currFilter['target'] + '&'

		for currInclude in includes:
			baseURL = baseURL + 'include=' + currInclude + '&'

		baseURL = baseURL[:-1]

	return baseURL

def getGeneric(target):
	# filters = [{'object': 'event.competitionId', 'target': '2e0f134b-a76f-46e9-b1bf-e1c987a11747'}]
	# includes = ['event.competition', 'event.competition.competitionType', 'event.competition.competitionType.competitionCategory']

	objects = []
	url = getData(target.endpoint)
	print(url)
	jsondata = json.loads(requests.get(url).content)['data']

	for thing in jsondata:
		newthing = target(**thing)
		objects.append(newthing)

	return objects