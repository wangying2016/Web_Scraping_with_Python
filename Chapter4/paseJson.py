import json
from urllib.request import urlopen
from pprint import pprint


def getCountry(ipAddress):
    response = urlopen('http://freegeoip.net/json/' + ipAddress
                       ).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson

pprint(getCountry('115.236.48.202'))
