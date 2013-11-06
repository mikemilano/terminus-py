from api import api, \
    user
from user import User

BASE_URL = 'https://terminus.getpantheon.com'
LURL = BASE_URL + '/login'
TURL = BASE_URL + '/terminus.php'


def auth(email, password):
    """
    Returns a User object with valid credentials.
    """
    session = api.auth(email, password)
    properties = user.info(session)
    return User(session, properties)
