import json
import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://terminus.getpantheon.com'
LURL = BASE_URL + '/login'
TURL = BASE_URL + '/terminus.php'


def auth(email, password):
    """
    Authenticates and generates a session

    Args:
        email: account email address
        password: account password

    Returns:
        request.Session object

    Raises:
        Error: on invalid authentication
    """
    session = requests.Session()
    response = session.get(LURL, verify=False)
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
    response = session.post(LURL, data=payload, allow_redirects=False, verify=False)

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


def request(session, payload, method='GET', data=None):
    if method == 'GET':
        return handle_response(session.get(TURL, params=payload))

    session.headers.update({'Content-Type': 'application/json'})
    data = json.dumps({'data': data})
    methods = {
        'POST': request_post,
        'PUT': request_put,
        'DELETE': request_delete
    }
    return handle_response(methods[method](session, payload, data))


def request_post(session, payload, data):
    return session.post(TURL, params=payload, data=data)


def request_put(session, payload, data):
    return session.put(TURL, params=payload, data=data)


def request_delete(session, payload, data):
    return session.delete(TURL, params=payload, data=data)


def handle_response(response):
    """
    Handles response

    Raises:
        Error: on status codes other than 200
    """
    if response.status_code == 200:
        try:
            return response.json()
        except:
            return response.content
    else:
        raise Exception('Error')