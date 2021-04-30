##################################################
## Weather API: This script creates a database of
## selected city reports from openweathermap.org
##################################################
## Author: Mark Chesney
## License: MIT license
## Version: 1.0
## Python Version: 3.9.2
## Email: mark.chesney@gmail.com
##################################################
## Packages Required
## peewee, datetime, pytz, requests, configparser,

from database import Report, read_csv, create_table, populate_table

# read in data from csv file
cities = read_csv('cities.csv')

# input data constraint: 25 cities
if len(cities) != 25:
    print('Warning: 25 cities are requested.')

# database is created in database module

# create table within database
create_table()

print('Inserting city weather reports:')
populate_table(cities)

# query database to verify
print("HOTTEST city, database query: {0.city}.\n".format(
    Report.select().order_by(Report.temp_F.desc()).get()
))

print("COOLEST city, database query: {0.city}.\n".format(
    Report.select().order_by(Report.temp_F.asc()).get()
))


###########
import requests, json
from util import build_http_req, parse_to_record
from database import _add_report

new_request = build_http_req(city='Laredo', state='TX',
                             country='US', units='imperial')

# call HTTP get method; store response to new_request
resp: requests.models.Response = requests.get(new_request)

# convert text attribute to JSON format
metadata = json.loads(resp.text)

# parse metadata into record
record = parse_to_record(metadata)

# store record into database
_add_report(record)

#   -   -   -   -
new_request = build_http_req(city='Fairbanks', state='AK',
                             country='US', units='imperial')

# call HTTP get method; store response to new_request
resp: requests.models.Response = requests.get(new_request)

# convert text attribute to JSON format
metadata = json.loads(resp.text)

# parse metadata into record
record = parse_to_record(metadata)

# store record into database
_add_report(record)
print()

#   -   -   -   -

# query database to verify
print("HOTTEST city, database query: {0.city}.\n".format(
    Report.select().order_by(Report.temp_F.desc()).get()
))

print("COOLEST city, database query: {0.city}.\n".format(
    Report.select().order_by(Report.temp_F.asc()).get()
))
