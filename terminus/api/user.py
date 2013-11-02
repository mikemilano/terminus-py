import api
import urllib


def info(session, user_uuid=None):
    """
    API call to get a user's information
    """
    if user_uuid is None:
        user_uuid = session.cookies.get('uuid')
    payload = {'user': user_uuid, 'path': ''}
    return api.request(session, payload)


def profile(session, values=None):
    """
    API call to get/set a user's profile
    """
    if values is None:
        payload = {'user': session.cookies.get('uuid'), 'path': 'profile'}
        return api.request(session, payload)
    else:
        payload = {'user': session.cookies.get('uuid'), 'path': 'profile'}
        return api.request(session, payload, 'PUT', values)


def attribute(session, attribute, value=None):
    """
    API call to get/set a field from a user's profile
    """
    if value is None:
        payload = {'user': session.cookies.get('uuid'), 'path': 'profile/'+attribute}
        return api.request(session, payload)
    else:
        payload = {'user': session.cookies.get('uuid'), 'path': 'profile/'+attribute}
        return api.request(session, payload, 'PUT', value)


def password(session, password):
    """
    API call to set a user's password
    """
    payload = {'user': session.cookies.get('uuid'), 'path': 'password'}
    return api.request(session, payload, 'PUT', password)


def email(session, email=None):
    """
    API call to get/set a user's email
    """
    if email is None:
        payload = {'user': session.cookies.get('uuid'), 'path': 'email'}
        return api.request(session, payload)
    else:
        payload = {'user': session.cookies.get('uuid'), 'path': 'email'}
        return api.request(session, payload, 'PUT', email)


def uuid(session, email):
    """
    API call to get a user's uuid
    """
    payload = {'user': session.cookies.get('uuid'), 'path': urllib.quote(email)+'/uuid'}
    return api.request(session, payload)


def check_email_by_email(session, email):
    """
    API call to check a user's email by email
    """
    payload = {'user': session.cookies.get('uuid'), 'path': urllib.quote(email)+'/email'}
    return api.request(session, payload)


def delete(session):
    """
    API call to delete a user
    """
    payload = {'user': session.cookies.get('uuid'), 'path': ''}
    return api.request(session, payload, 'DELETE')


def keys(session):
    """
    API call to get a user's ssh keys
    """
    payload = {'user': session.cookies.get('uuid'), 'path': 'keys'}
    return api.request(session, payload)


def add_key(session, key):
    """
    API call to add a ssh key
    """
    payload = {'user': session.cookies.get('uuid'), 'path': 'keys'}
    return api.request(session, payload, 'POST', key)


def delete_key(session, key):
    """
    API call to delete a specific ssh key
    """
    payload = {'user': session.cookies.get('uuid'), 'path': 'keys/'+key}
    return api.request(session, payload, 'DELETE')


def delete_keys(session):
    """
    API call to delete a user's ssh keys
    """
    payload = {'user': session.cookies.get('uuid'), 'path': 'keys'}
    return api.request(session, payload, 'DELETE')


def validate_key(session, key):
    """
    API call to add and validate ssh key
    """
    payload = {'user': session.cookies.get('uuid'), 'path': 'keys?validate=true'}
    return api.request(session, payload, 'POST', key)


def sites(session):
    """
    API call to get a list of sites a user is a team member of
    """
    payload = {'user': session.cookies.get('uuid'), 'path': 'sites'}
    return api.request(session, payload)


def owned_sites(session):
    """
    API call to get a list of sites owned by a user
    """
    payload = {'user': session.cookies.get('uuid'), 'path': 'sites?owned=1'}
    return api.request(session, payload)