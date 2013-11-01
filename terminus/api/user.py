import api


def info(session):
    payload = {'user': session.cookies.get('uuid'), 'path': ''}
    return api.request(session, payload)


def profile(session, profile=None):
    if profile is None:
        payload = {'user': session.cookies.get('uuid'), 'path': 'profile'}
        return api.request(session, payload)
    else:
        payload = {'user': session.cookies.get('uuid'), 'path': 'profile'}
        return api.request(session, payload, 'PUT', profile)


def attribute(session, attribute, value=None):
    if value is None:
        payload = {'user': session.cookies.get('uuid'), 'path': 'profile/'+attribute}
        return api.request(session, payload)
    else:
        payload = {'user': session.cookies.get('uuid'), 'path': 'profile/'+attribute}
        return api.request(session, payload, 'PUT', value)


def password(session, password):
    payload = {'user': session.cookies.get('uuid'), 'path': 'password'}
    return api.request(session, payload, 'PUT', password)


def email(session, email=None):
    if email is None:
        payload = {'user': session.cookies.get('uuid'), 'path': 'email'}
        return api.request(session, payload)
    else:
        payload = {'user': session.cookies.get('uuid'), 'path': 'email'}
        return api.request(session, payload, 'PUT', email)


def uuid(session, email):
    payload = {'user': session.cookies.get('uuid'), 'path': email+'/uuid'}
    return api.request(session, payload)


def check_email_by_email(session, email):
    payload = {'user': session.cookies.get('uuid'), 'path': email+'/email'}
    return api.request(session, payload)


def delete(session):
    payload = {'user': session.cookies.get('uuid'), 'path': ''}
    return api.request(session, payload, 'DELETE')


def keys(session):
    payload = {'user': session.cookies.get('uuid'), 'path': 'keys'}
    return api.request(session, payload)


def add_key(session, key):
    payload = {'user': session.cookies.get('uuid'), 'path': 'keys'}
    return api.request(session, payload, 'POST', key)


def delete_key(session, key):
    payload = {'user': session.cookies.get('uuid'), 'path': 'keys/'+key}
    return api.request(session, payload, 'DELETE')


def delete_keys(session):
    payload = {'user': session.cookies.get('uuid'), 'path': 'keys'}
    return api.request(session, payload, 'DELETE')


def validate_key(session, key):
    payload = {'user': session.cookies.get('uuid'), 'path': 'keys?validate=true'}
    return api.request(session, payload, 'POST', key)


def sites(session):
    payload = {'user': session.cookies.get('uuid'), 'path': 'sites'}
    return api.request(session, payload)


def owned_sites(session):
    payload = {'user': session.cookies.get('uuid'), 'path': 'sites?owned=1'}
    return api.request(session, payload)