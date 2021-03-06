import requests
from peewee import *
import csv
import os

from util import build_http_req, parse_to_record

# variable scope: global across this module
# SQLite selected for its straightforward implementation and high reliability
weather_db = SqliteDatabase('weather.db')

class Report(Model):
    city_id = BigIntegerField(unique=True)
    city = CharField(max_length=255, unique=True)
    time_est = DateTimeField()
    weather = CharField(max_length=255)
    temp_F = FloatField()
    feels_like = FloatField()

    class Meta:
        database = weather_db


def read_csv(fn):
    """
    read in csv data

    Parameters
    ----------
    fn : str
        filename

    Returns
    -------
    list
    """
    arr = []
    with open(fn, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            arr.append(row)
    return arr


def create_table():
    """
    create table within database
    """
    # must delete old DB, and initialize new DB, to continue
    _prompt_overwrite()

    weather_db.connect()
    weather_db.create_tables([Report], safe=True)


def populate_table(locations):
    """
    populate table within database, specifically with city weather reports
    
    Parameters
    ----------
    locations : list
        nested lists
        indices are: [0] city name; [1] state code (US only); [2] country code
    """
    for loc in locations:
        # construct HTTP request for openweathermap API

        if loc[1] is not None:   # city in USA (i.e., city has a state code)
            request = build_http_req(city=loc[0], state=loc[1],
                                     country=loc[-1], units='imperial')
        else:
            request = build_http_req(city=loc[0],
                                     country=loc[-1], units='imperial')

        # call HTTP get method; store response to request
        resp: requests.models.Response = requests.get(request)

        # convert text attribute to JSON format
        metadata = resp.json()

        # parse metadata into record
        record = parse_to_record(metadata)
        # store record into database
        add_report(record)
    print()


def add_report(rec, display=True):
    """
    insert a record into the database

    Parameters
    ----------
    rec : dict
        weather report of 1 city
    display : bool
        print name of city after insertion
    """
    Report.create(city_id=rec['city_id'],
                  city=rec['city'],
                  time_est=rec['time_est'],
                  weather=rec['weather'],
                  temp_F=rec['temp_F'],
                  feels_like=rec['feels_like']
                  )
    if display:
        print(rec['city'])


def _prompt_overwrite():
    """
    Ask user to overwrite old DB file, to initialize a new one
    """
    if os.path.exists('weather.db'):
        key = input('Overwrite weather.db? (Y/n): ')
        if key != 'n':
            os.remove('weather.db')
        else:
            print('Exiting...')
            quit()
