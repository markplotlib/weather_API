import requests
import json

from util import build_http_req, parse_to_record

# construct HTTP request for openweathermap API
request = build_http_req(city='Honolulu', state='HI',
                         country='US', units='imperial')

# call HTTP get method; store response to request
resp: requests.models.Response = requests.get(request)

# convert text attribute to JSON format
metadata = json.loads(resp.text)

# parse metadata into record
rec = parse_to_record(metadata)

# table header
header = ('city_id', 'city', 'time_est', 'weather', 'temperature', 'feels_like')

# store in database
