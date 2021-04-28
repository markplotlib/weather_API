import configparser
import requests
import json
from datetime import datetime

from util import to_timezone, parse_to_record

# read in token
parser = configparser.ConfigParser()
parser.read('token.cfg')
TOKEN = parser['openweathermap']['token']

# get weather -- 1 city
# location inputs
CITY='Honolulu'
STATE='HI'
COUNTRY='US'

# connect to openweathermap
request = 'http://api.openweathermap.org/data/2.5/weather' \
          + '?q={city},{state},{country}&appid={key}&units=imperial'.format(
          city=CITY, state=STATE, country=COUNTRY, key=TOKEN)

# call HTTP get method; store response to request
resp: requests.models.Response = requests.get(request)

# convert text attribute to JSON format
metadata = json.loads(resp.text)

# parse metadata into record
rec = parse_to_record(metadata)

# store in database
