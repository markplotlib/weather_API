import requests
import json
from peewee import *

from util import prompt_overwrite, build_http_req, parse_to_record
from db import Report, add_report, hottest, coolest, CITIES

if len(CITIES) != 25:
    raise ValueError('25 cities required.')

# must delete old DB, and initialize new DB, to continue
prompt_overwrite()

# SQLite selected for its straightforward implementation
weather_db = SqliteDatabase('weather.db')
weather_db.connect()
weather_db.create_tables([Report], safe=True)

print('Inserting city weather reports:')
for city in CITIES:
    # construct HTTP request for openweathermap API
    request = build_http_req(city=city,
                         country='JP', units='imperial')

    # call HTTP get method; store response to request
    resp: requests.models.Response = requests.get(request)

    # convert text attribute to JSON format
    metadata = json.loads(resp.text)

    # parse metadata into record
    record = parse_to_record(metadata)
    add_report(record)

print()

# store in database
print("Database query for the hottest city: {0.city}.".format(hottest()))
print("Database query for the coolest city: {0.city}.".format(coolest()))
