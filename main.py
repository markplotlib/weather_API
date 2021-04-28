import requests
import json

from util import build_http_req, parse_to_record

# selection: 25 cities
cities = ['Tokyo', 'Nagoya', 'Kyoto'
          # , 'Nara', 'Osaka', 'Himeji',
          # , 'Hiroshima', 'Fukuoka', 'Sapporo', 'Hakodate', 'Otaru'
          # , 'Abashiri', 'Shari', 'Kushiro', 'Akita', 'Saitama', 'Ise'
          # , 'Takayama', 'Yamagata', 'Nikko', 'Tateyama', 'Naha'
          # , 'Kagoshima', 'Nagano', 'Hikone'
          ]

for city in cities:
    # construct HTTP request for openweathermap API
    request = build_http_req(city=city,
                         country='JP', units='imperial')

    # call HTTP get method; store response to request
    resp: requests.models.Response = requests.get(request)

    # convert text attribute to JSON format
    metadata = json.loads(resp.text)

    # parse metadata into record
    rec = parse_to_record(metadata)
    print(rec)

# table header
header = ('city_id', 'city', 'time_est', 'weather', 'temperature', 'feels_like')

# store in database
