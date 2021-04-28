import configparser
import requests
import json
from datetime import datetime

from util import to_timezone

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
meta = json.loads(resp.text)


###### parse meta dictionary
# a.	City ID
id = meta['id']

# b.	City name
name = meta['name']

# c.	Datetime – convert from Unix timestamp to EST
ts = meta['dt']
utc: datetime = datetime.utcfromtimestamp(ts)
est: datetime = to_timezone(utc, 'US/Eastern')

# d.	Weather description
desc = meta['weather'][0]['description']

# e.	Current temperature
temp_F = meta['main']['temp']

# f.	Feels like temperature
temp_feels = meta['main']['feels_like']
######

print(id, name, est, desc, temp_F, temp_feels, sep='; ')

# table header
header = 'city_id', 'city', 'time_est', 'weather', 'temperature', 'feels_like'

# store in database
