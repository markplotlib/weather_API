import requests, json
from util import build_http_req, parse_to_record
from database import Report, read_csv, create_table, populate_table, add_report

def db_pipeline(city, state, country):
    new_request = build_http_req(city=city, state=state,
                                 country=country, units='imperial')

    # call HTTP get method; store response to new_request
    resp: requests.models.Response = requests.get(new_request)

    # convert text attribute to JSON format
    metadata = json.loads(resp.text)

    # parse metadata into record
    record = parse_to_record(metadata)

    # store record into database
    add_report(record)

#   -   -   -   -
db_pipeline(city='Laredo', state='TX', country='US')
db_pipeline(city='Fairbanks', state='AK', country='US')
print()

#   -   -   -   -

# query database to verify
print("HOTTEST city, database query: {0.city}.\n".format(
    Report.select().order_by(Report.temp_F.desc()).get()
))

print("COOLEST city, database query: {0.city}.\n".format(
    Report.select().order_by(Report.temp_F.asc()).get()
))
