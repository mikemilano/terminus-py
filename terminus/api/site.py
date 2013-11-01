import api
import urllib


def info(session, uuid):
    payload = {'site': uuid, 'path': ''}
    return api.request(session, payload)


def state(session, uuid):
    payload = {'site': uuid, 'path': 'state'}
    return api.request(session, payload)


def delete(session, uuid):
    payload = {'site': uuid, 'path': ''}
    return api.request(session, payload, 'DELETE')


def settings(session, uuid):
    payload = {'site': uuid, 'path': 'settings'}
    return api.request(session, payload)


def service_level(session, uuid, value=None):
    payload = {'site': uuid, 'path': 'service-level'}
    if value is None:
        return api.request(session, payload)
    else:
        return api.request(session, payload, 'PUT', value)


def attribute(session, uuid, key, value=None):
    payload = {'site': uuid, 'path': 'attributes/'+key}
    if value is None:
        return api.request(session, payload)
    else:
        return api.request(session, payload, 'PUT', value)


def attributes(session, uuid, values=None):
    payload = {'site': uuid, 'path': 'attributes'}
    if values is None:
        return api.request(session, payload)
    else:
        return api.request(session, payload, 'PUT', values)


def delete_attributes(session, uuid):
    payload = {'site': uuid, 'path': 'attributes'}
    return api.request(session, payload, 'DELETE')


def upstream(session, uuid):
    payload = {'site': uuid, 'path': 'code-upstream'}
    return api.request(session, payload)


def team_members(session, uuid):
    payload = {'site': uuid, 'path': 'team'}
    return api.request(session, payload)


def is_team_member(session, uuid, user_uuid):
    payload = {'site': uuid, 'path': 'team/'+user_uuid}
    return api.request(session, payload)


def delete_team_member(session, uuid, user_uuid):
    payload = {'site': uuid, 'path': 'team/'+user_uuid}
    return api.request(session, payload, 'DELETE')


def invite_team_member(session, uuid, email, invited_by):
    payload = {'site': uuid, 'path': 'team/'+urllib.quote(email)}
    data = {'invited_by': invited_by}
    return api.request(session, payload, 'POST', data)


def owner(session, uuid):
    payload = {'site': uuid, 'path': 'owner'}
    return api.request(session, payload)


def notifications(session, uuid):
    payload = {'site': uuid, 'path': 'notifications'}
    return api.request(session, payload)


def screenshot(session, uuid):
    payload = {'site': uuid, 'path': 'generate-screenshots'}
    return api.request(session, payload, 'POST')


def environments(session, uuid):
    payload = {'site': uuid, 'path': 'environments'}
    return api.request(session, payload)


def binding(session, uuid, environment, type):
    payload = {'site': uuid, 'path': 'environment/'+environment+'/bindings?type='+type}
    return api.request(session, payload)


def bindings(session, uuid, environment):
    payload = {'site': uuid, 'path': 'environment/'+environment+'/bindings'}
    return api.request(session, payload)


def events(session, uuid, environment, limit=100):
    payload = {'site': uuid, 'path': 'environments/'+environment+'?limit='+limit}
    return api.request(session, payload)


def clear_cache(session, uuid, environment):
    payload = {'site': uuid, 'path': 'environment/'+environment+'/clear-cache'}
    return api.request(session, payload, 'POST')


def onserver_status(session, uuid, environment, value=None):
    payload = {'site': uuid, 'path': 'environments/'+environment+'/on-server-development'}
    if value is None:
        return api.request(session, payload)
    else:
        data = {'enabled': value}
        return api.request(session, payload, 'PUT', data)


def onserver_commit(session, uuid, environment, message=None):
    payload = {'site': uuid, 'path': 'environments/'+environment+'/on-server-development/commit'}
    if message is None:
        data = ''
    else:
        data = {'message': message}
    return api.request(session, payload, 'PUT', data)


def onserver_diff(session, uuid, environment, filepath):
    payload = {'site': uuid, 'path': 'environments/'+environment+'/on-server-development/diff?path='+urllib.quote(filepath)}
    return api.request(session, payload)


def onserver_diff_stats(session, uuid, environment):
    payload = {'site': uuid, 'path': 'environments/'+environment+'/on-server-development/diffstat'}
    return api.request(session, payload)


def lock(session, uuid, environment, username, password):
    payload = {'site': uuid, 'path': 'environments/'+environment+'/lock'}
    data = {'username': username, 'password': password}
    return api.request(session, payload, 'PUT', data)


def delete_lock(session, uuid, environment):
    payload = {'site': uuid, 'path': 'environments/'+environment+'/lock'}
    return api.request(session, payload, 'DELETE')


def hostnames(session, uuid, environment):
    payload = {'site': uuid, 'path': 'environments/'+environment+'/hostnames'}
    return api.request(session, payload)


def add_hostname(session, uuid, environment, hostname):
    payload = {'site': uuid, 'path': 'environments/'+environment+'/hostnames/'+urllib.quote(hostname)}
    return api.request(session, payload, 'PUT')


def delete_hostname(session, uuid, environment, hostname):
    payload = {'site': uuid, 'path': 'environments/'+environment+'/hostnames/'+urllib.quote(hostname)}
    return api.request(session, payload, 'DELETE')