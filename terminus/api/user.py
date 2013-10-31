import api


def info(session):
    payload = {'user': session.cookies.get('uuid'), 'path': ''}
    response = session.get(api.TURL, params=payload)
    return api.handle_response(response)


def profile(session, profile=None):
    response = None
    if profile is None:
        payload = {'user': session.cookies.get('uuid'), 'path': 'profile'}
        response = session.get(api.TURL, params=payload)

    #TODO: Handle set profile
    return api.handle_response(response)


#def set_profile(session, profile):
#    return None


#def update_profile(session, profile):
#    return None


def attribute(session, attribute, value=None):
    response = None
    if value is None:
        payload = {'user': session.cookies.get('uuid'), 'path': 'profile/'+attribute}
        response = session.get(api.TURL, params=payload)
    #TODO: Handle set attribute
    return api.handle_response(response)


#def set_attribute(session, attribute):
#    return None


def password(session, password):
    return None


def email(session, email=None):
    response = None
    if email is None:
        payload = {'user': session.cookies.get('uuid'), 'path': 'email'}
        response = session.get(api.TURL, params=payload)
    #TODO: Handle set email
    return api.handle_response(response)


#def set_email(session, email):
#    return None


def get_uuid(session, email):
    return None


def get_email_by_email(session, email):
    return None


def delete(session):
    return None


def keys(session):
    payload = {'user': session.cookies.get('uuid'), 'path': 'keys'}
    response = session.get(api.TURL, params=payload)
    return api.handle_response(response)


def add_key(session, key):
    return None


def delete_keys(session):
    return None


def validate_key(session, key):
    return None


def sites(session):
    payload = {'user': session.cookies.get('uuid'), 'path': 'sites'}
    response = session.get(api.TURL, params=payload)
    return api.handle_response(response)


def owned_sites(session):
    payload = {'user': session.cookies.get('uuid'), 'path': 'sites?owned=1'}
    response = session.get(api.TURL, params=payload)
    return api.handle_response(response)