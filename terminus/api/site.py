import api


def info(session, uuid):
    payload = {'site': uuid, 'path': ''}
    response = session.get(api.TURL, params=payload)
    return api.handle_response(response)


def state(session, uuid):
    payload = {'site': uuid, 'path': 'state'}
    response = session.get(api.TURL, params=payload)
    return api.handle_response(response)


def delete(session, uuid):
    return None


def settings(session, uuid):
    payload = {'site': uuid, 'path': 'settings'}
    response = session.get(api.TURL, params=payload)
    return api.handle_response(response)


def get_service_level(session, uuid):
    payload = {'site': uuid, 'path': 'service-level'}
    response = session.get(api.TURL, params=payload)
    return api.handle_response(response)


def set_service_level(session, uuid, service_level):
    return None


def get_attribute(session, uuid, attribute):
    payload = {'site': uuid, 'path': 'attributes/'+attribute}
    response = session.get(api.TURL, params=payload)
    return api.handle_response(response)


def set_attribute(session, uuid, attribute, value):
    return None


def get_attributes(session, uuid):
    payload = {'site': uuid, 'path': 'attributes'}
    response = session.get(api.TURL, params=payload)
    return api.handle_response(response)


def set_attributes(session, uuid, attributes):
    return None


def delete_attributes(session, uuid):
    return None


def get_upstream(session, uuid):
    payload = {'site': uuid, 'path': 'code-upstream'}
    response = session.get(api.TURL, params=payload)
    return api.handle_response(response)


def get_team_members(session, uuid):
    payload = {'site': uuid, 'path': 'team'}
    response = session.get(api.TURL, params=payload)
    return api.handle_response(response)


def delete_team_member(session, uuid):
    return None


def invite_team_member(session, uuid, email, invited_by):
    return None


def verify_team_member(session, uuid, uid):
    return None


def get_owner(session, uuid):
    payload = {'site': uuid, 'path': 'owner'}
    response = session.get(api.TURL, params=payload)
    return api.handle_response(response)


def screenshot(session, uuid):
    return None


def events(session, uuid, environment, limit=100):
    payload = {'site': uuid, 'path': 'environments/'+environment+'?limit='+limit}
    response = session.get(api.TURL, params=payload)
    return api.handle_response(response)


def get_binding(session, uuid, environment, type):
    payload = {'site': uuid, 'path': 'environment/'+environment+'/bindings?type='+type}
    response = session.get(api.TURL, params=payload)
    return api.handle_response(response)


def get_bindings(session, uuid, environment):
    payload = {'site': uuid, 'path': 'environment/'+environment+'/bindings'}
    response = session.get(api.TURL, params=payload)
    return api.handle_response(response)


def clear_cache(session, uuid, environment):
    return None


def get_onserver_status(session, uuid, environment):
    payload = {'site': uuid, 'path': 'environments/'+environment+'/on-server-development'}
    response = session.get(api.TURL, params=payload)
    return api.handle_response(response)


def set_onserver_status(session, uuid, environment, status):
    return None


def commit(session, uuid, environment, message):
    return None


def diff(session, uuid, environment, filepath):
    payload = {'site': uuid, 'path': 'environments/'+environment+'/on-server-development/diffstat'}
    response = session.get(api.TURL, params=payload)
    return api.handle_response(response)


def diff_stats(session, uuid, environment):
    return None


def lock(session, uuid, environment, username, password):
    return None


def delete_lock(session, uuid, environment):
    return None


def hostnames(session, uuid, environment):
    payload = {'site': uuid, 'path': 'environments/'+environment+'/hostnames'}
    response = session.get(api.TURL, params=payload)
    return api.handle_response(response)


def add_hostname(session, uuid, environment, hostname):
    return None


def delete_hostname(session, uuid, environment, hostname):
    return None


def environments(session, uuid):
    payload = {'site': uuid, 'path': 'environments'}
    response = session.get(api.TURL, params=payload)
    return api.handle_response(response)


def notifications(session, uuid):
    payload = {'site': uuid, 'path': 'notifications'}
    response = session.get(api.TURL, params=payload)
    return api.handle_response(response)


def bindings(session, uuid):
    payload = {'site': uuid, 'path': 'bindings'}
    response = session.get(api.TURL, params=payload)
    return api.handle_response(response)