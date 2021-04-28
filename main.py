import configparser
import requests
import json
from datetime import datetime
import pytz

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

#   -   -   -   -   -
def to_timezone(dt, tz_name):
    """
    Converts dt to a target timezone

    Parameters
    ----------
    dt : datetime
        input datetime to convert
    tz_name : str
        timezone name, e.g. 'US/Hawaii'

    Returns
    -------
    datetime
        conversion to target timezone
    """
    local = pytz.utc.localize(dt)
    tz_target = pytz.timezone(tz_name)
    return local.astimezone(tz_target)

# c.	Datetime – convert from Unix timestamp to EST
ts = meta['dt']
utc: datetime = datetime.utcfromtimestamp(ts)
est: datetime = to_timezone(utc, 'US/Eastern')
#   -   -   -   -   -

# d.	Weather description
desc = meta['weather'][0]['description']

# e.	Current temperature
temp_F = meta['main']['temp']

# f.	Feels like temperature
temp_feels = meta['main']['feels_like']
######

print(id, name, est, desc, temp_F, temp_feels, sep='; ')

# store in database
