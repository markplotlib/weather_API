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
