from peewee import *

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


if __name__ == '__main__':
    # delete old DB, and initialize new DB
    import os
    if os.path.exists('weather.db'):
        key = input('Overwrite weather.db? (Y/n): ')
        if key != 'n':
            os.remove('weather.db')
        else:
            print('Exiting...')
            quit()

    weather_db.connect()
    weather_db.create_tables([Report], safe=True)
    add_report()
    print("The hottest city is: {0.city}.".format(hottest()))
    print("The coolest city is: {0.city}.".format(coolest()))
