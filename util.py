from datetime import datetime
import pytz

def to_timezone(dt, tz_name):
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
    est: datetime = to_timezone(utc, 'US/Eastern')
    str_est = str(est)

    # d.	Weather description
    desc = meta['weather'][0]['description']

    # e.	Current temperature
    temp_F = meta['main']['temp']

    # f.	Feels like temperature
    temp_feels = meta['main']['feels_like']

    return (id, name, str_est, desc, temp_F, temp_feels)
