import configparser
from datetime import datetime
import pytz

def build_http_req(**kwargs):
    """
    Construct request for HTTP get method

    Parameters
    ----------
    kwargs : dict
        key-word arguments specific to HTTP request

    Returns
    -------
    str
        HTTP request specific for openweathermap API
    """
    token = _get_token()

    req = 'http://api.openweathermap.org/data/2.5/weather' \
          + '?q={city},{state},{country}&appid={token}&units={units}'.format(
            **kwargs, token=token)

    return req


def parse_to_record(meta):
    """
    Parse metadata into 1 record

    Parameters
    ----------
    meta : dict
        metadata selected from this specific JSON object

    Returns
    -------
    tuple
        record of selected features
    """
    # a.	City ID
    id = meta['id']

    # b.	City name
    name = meta['name']

    # c.	Datetime – convert from Unix timestamp to EST
    ts = meta['dt']
    utc: datetime = datetime.utcfromtimestamp(ts)
    est: datetime = _to_timezone(utc, 'US/Eastern')
    str_est = str(est)

    # d.	Weather description
    desc = meta['weather'][0]['description']

    # e.	Current temperature
    temp_F = meta['main']['temp']

    # f.	Feels like temperature
    temp_feels = meta['main']['feels_like']

    return (id, name, str_est, desc, temp_F, temp_feels)


def _to_timezone(dt, tz_name):
    """
    Converts dt to a target timezone

    Parameters
    ----------
    dt : datetime
        input datetime to convert
    tz_name : str
        timezone name, e.g. 'US/Hawaii'

    Returns
    -------
    datetime
        conversion to target timezone
    """
    local = pytz.utc.localize(dt)
    tz_target = pytz.timezone(tz_name)
    return local.astimezone(tz_target)


def _get_token(filename='token.cfg', key_ring='openweathermap'):
    """
    read in API token

    Parameters
    ----------
    filename : str
        local file with API token
    key_ring : str
        dictionary key, appearing within [] in token file

    Returns
    -------
    str
        API token
    """
    parser = configparser.ConfigParser()
    parser.read(filename)
    return parser[key_ring]['token']
