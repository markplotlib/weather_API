from peewee import *
import os

# selection: 25 cities
CITIES = ['Tokyo', 'Nagoya', 'Kyoto' \
          , 'Nara', 'Himeji', 'Osaka', 'Aomori' \
          , 'Hiroshima', 'Fukuoka', 'Sapporo', 'Hakodate', 'Otaru' \
          , 'Naha' , 'Abashiri', 'Kushiro', 'Akita', 'Saitama' \
          , 'Takayama', 'Yamagata', 'Nikko', 'Tateyama', 'Ise' \
          , 'Kagoshima', 'Nagano', 'Hikone' \
          ]

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


def create_db_table(fn):
    """
    create single-table database

    Parameters
    ----------
    fn : str
        DB filename
    """
    # must delete old DB, and initialize new DB, to continue
    _prompt_overwrite()

    weather_db.connect()
    weather_db.create_tables([Report], safe=True)


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


def hottest():
    return Report.select().order_by(Report.temp_F.desc()).get()

def coolest():
    return Report.select().order_by(Report.temp_F.asc()).get()

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
