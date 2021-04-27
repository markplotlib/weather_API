import configparser
import requests

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
          + '?q={city},{state},{country}&appid={key}'.format(
          city=CITY, state=STATE, country=COUNTRY, key=TOKEN)




# store in database
