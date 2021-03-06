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
locations = read_csv('cities.csv')

# input data constraint: 25 locations
if len(locations) != 25:
    print('Warning: 25 cities are requested.')

# database is created in database module

# create table within database
create_table()

print('Inserting city weather reports:')
populate_table(locations)

# query database to verify
print("HOTTEST city, database query: {0.city}.\n".format(
    Report.select().order_by(Report.temp_F.desc()).get()
))

print("COOLEST city, database query: {0.city}.\n".format(
    Report.select().order_by(Report.temp_F.asc()).get()
))
