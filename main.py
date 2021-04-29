##################################################
## Weather API: This script creates a database of
## selected city reports from openweathermap.org
##################################################
## Author: Mark Chesney
## License: MIT license
## Version: 1.0
## Email: mark.chesney@gmail.com
##################################################

from db import Report, create_table, populate_table, CITIES

# input data constraint: 25 cities
if len(CITIES) != 25:
    print('Warning: 25 cities are requested.')

# (database is created in db module)

# create table within SQLite database
# SQLite is selected for its straightforward implementation and high reliability
create_table()

print('Inserting city weather reports:')
populate_table()

# query database to verify
print("HOTTEST city, database query: {0.city}.".format(
    Report.select().order_by(Report.temp_F.desc()).get()
))

print("COOLEST city, database query: {0.city}.".format(
    Report.select().order_by(Report.temp_F.asc()).get()
))
