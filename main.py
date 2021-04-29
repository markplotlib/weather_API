import requests
import json

from util import build_http_req, parse_to_record
from db import Report, create_table, add_report, hottest, coolest, CITIES

if len(CITIES) != 25:
    raise ValueError('25 cities required.')

# create table within SQLite database (which is created in db.py module)
# SQLite is selected for its straightforward implementation and high reliability
create_table()

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
    # store record into database
    add_report(record)
print()

# query database to verify
print("Database query for the hottest city: {0.city}.".format(hottest()))
print("Database query for the coolest city: {0.city}.".format(coolest()))
