import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://terminus.getpantheon.com'
LURL = BASE_URL + '/login'
TURL = BASE_URL + '/terminus.php'

session = None

def auth(email, password):
    """
    Authenticates and generates a session

    Args:
        email: account email address
        password: account password

    Returns:
        User

    Raises:
        Error: on invalid authentication
    """
    session = requests.Session()
    response = session.get(LURL)
    soup = BeautifulSoup(response.text)
    form_build_id = ''

    for element in soup.find_all('input'):
        if element.get('name') == 'form_build_id':
            form_build_id = element.get('value')
            break

    payload = {
        'email': email,
        'password': password,
        'form_build_id': form_build_id,
        'form_id': 'atlas_login_form',
        'op': 'Login'
    }
    response = session.post(LURL, data=payload, allow_redirects=False)

    setcookie = response.headers.get('set-cookie')
    valid_session = False

    for cookie in session.cookies:
        if cookie.name.startswith('SSESS'):
            valid_session = True

    if setcookie is None or not valid_session:
        raise Exception('Authentication failure')

    arr = response.headers.get('location').rsplit('/', 1)
    uuid = arr[1]
    session.cookies.set('uuid', uuid)
    return session


def handle_response(response):
    """
    Handles response
    """
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception('Dashboard unavailable')