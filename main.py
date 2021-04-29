from db import Report, create_table, populate_table, CITIES

# input data constraint: 25 cities
if len(CITIES) != 25:
    print('Warning: 25 cities are requested.')

# create table within SQLite database (which is created in db.py module)
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
