# read in token
import configparser
parser = configparser.ConfigParser()
parser.read('token.cfg')
token = parser['openweathermap']['token']
print(token)

# connect to openweathermap

# get weather -- 1 city
    # api.openweathermap.org/data/2.5/weather?q={city name},{state code},{country code}&appid={API key}

# store in database
