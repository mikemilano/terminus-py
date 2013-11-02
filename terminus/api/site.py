import api
import urllib


def info(session, uuid):
    """
    API call get the quick site info
    """
    payload = {'site': uuid, 'path': ''}
    return api.request(session, payload)


def state(session, uuid):
    """
    API call get the site omnibus "state"
    """
    payload = {'site': uuid, 'path': 'state'}
    return api.request(session, payload)


def delete(session, uuid):
    """
    API call to delete a site
    """
    payload = {'site': uuid, 'path': ''}
    return api.request(session, payload, 'DELETE')


def settings(session, uuid):
    """
    API call to get/set site settings
    """
    payload = {'site': uuid, 'path': 'settings'}
    return api.request(session, payload)


def service_level(session, uuid, value=None):
    """
    API call to get/set site service level
    """
    payload = {'site': uuid, 'path': 'service-level'}
    if value is None:
        return api.request(session, payload)
    else:
        return api.request(session, payload, 'PUT', value)


def attribute(session, uuid, key, value=None):
    """
    API call to get/set one site attribute
    """
    payload = {'site': uuid, 'path': 'attributes/'+key}
    if value is None:
        return api.request(session, payload)
    else:
        return api.request(session, payload, 'PUT', value)


def attributes(session, uuid, values=None):
    """
    API call to get/set all site attributes at once
    """
    payload = {'site': uuid, 'path': 'attributes'}
    if values is None:
        return api.request(session, payload)
    else:
        return api.request(session, payload, 'PUT', values)


def delete_attributes(session, uuid):
    """
    API call to delete site attributes
    """
    payload = {'site': uuid, 'path': 'attributes'}
    return api.request(session, payload, 'DELETE')


def upstream(session, uuid):
    """
    API call to get site upstream
    """
    payload = {'site': uuid, 'path': 'code-upstream'}
    return api.request(session, payload)


def team_members(session, uuid):
    """
    API call to get list of users from a site team
    """
    payload = {'site': uuid, 'path': 'team'}
    return api.request(session, payload)


def is_team_member(session, uuid, user_uuid):
    """
    API call to check user against the list of users from a site team
    """
    payload = {'site': uuid, 'path': 'team/'+user_uuid}
    return api.request(session, payload)


def delete_team_member(session, uuid, user_uuid):
    """
    API call to delete a user from a site team
    """
    payload = {'site': uuid, 'path': 'team/'+user_uuid}
    return api.request(session, payload, 'DELETE')


def invite_team_member(session, uuid, email, invited_by):
    """
    API call to invite a user to Pantheon and add to site team
    """
    payload = {'site': uuid, 'path': 'team/'+urllib.quote(email)}
    data = {'invited_by': invited_by}
    return api.request(session, payload, 'POST', data)


def owner(session, uuid):
    """
    API call to get the user_uuid of the site owner
    """
    payload = {'site': uuid, 'path': 'owner'}
    return api.request(session, payload)


def notifications(session, uuid):
    """
    API call to get notifications for a site to track job status
    """
    payload = {'site': uuid, 'path': 'notifications'}
    return api.request(session, payload)


def screenshot(session, uuid):
    """
    API call to take site screenshots
    """
    payload = {'site': uuid, 'path': 'generate-screenshots'}
    return api.request(session, payload, 'POST')


def environments(session, uuid):
    """
    API call to get environments for an site
    """
    payload = {'site': uuid, 'path': 'environments'}
    return api.request(session, payload)


def binding(session, uuid, environment, type):
    """
    API call to get bindings for a site
    """
    payload = {'site': uuid, 'path': 'environment/'+environment+'/bindings?type='+type}
    return api.request(session, payload)


def bindings(session, uuid, environment):
    """
    API call to get all bindings for a site to track spin-up status
    """
    payload = {'site': uuid, 'path': 'environment/'+environment+'/bindings'}
    return api.request(session, payload)


def events(session, uuid, environment, limit=100):
    """
    API call to get events
    """
    payload = {'site': uuid, 'path': 'environments/'+environment+'?limit='+limit}
    return api.request(session, payload)


def clear_cache(session, uuid, environment):
    """
    API call to clear caches
    """
    payload = {'site': uuid, 'path': 'environment/'+environment+'/clear-cache'}
    return api.request(session, payload, 'POST')


def onserver_status(session, uuid, environment, value=None):
    """
    API call to get/set on-sserver development status
    """
    payload = {'site': uuid, 'path': 'environments/'+environment+'/on-server-development'}
    if value is None:
        return api.request(session, payload)
    else:
        data = {'enabled': value}
        return api.request(session, payload, 'PUT', data)


def onserver_commit(session, uuid, environment, message=None):
    """
    API call to do an on-server git commit
    """
    payload = {'site': uuid, 'path': 'environments/'+environment+'/on-server-development/commit'}
    if message is None:
        data = ''
    else:
        data = {'message': message}
    return api.request(session, payload, 'PUT', data)


def onserver_diff(session, uuid, environment, filepath):
    """
    API call to get an on-server git diff of a path
    """
    payload = {'site': uuid, 'path': 'environments/'+environment+'/on-server-development/diff?path='+urllib.quote(filepath)}
    return api.request(session, payload)


def onserver_diff_stats(session, uuid, environment):
    """
    API call to get an on-server git diff --numstat
    """
    payload = {'site': uuid, 'path': 'environments/'+environment+'/on-server-development/diffstat'}
    return api.request(session, payload)


def lock(session, uuid, environment, username, password):
    """
    API call to lock an environment
    """
    payload = {'site': uuid, 'path': 'environments/'+environment+'/lock'}
    data = {'username': username, 'password': password}
    return api.request(session, payload, 'PUT', data)


def delete_lock(session, uuid, environment):
    """
    API call to delete a lock on an environment
    """
    payload = {'site': uuid, 'path': 'environments/'+environment+'/lock'}
    return api.request(session, payload, 'DELETE')


def hostnames(session, uuid, environment):
    """
    API call to get hostnames for an environment
    """
    payload = {'site': uuid, 'path': 'environments/'+environment+'/hostnames'}
    return api.request(session, payload)


def add_hostname(session, uuid, environment, hostname):
    """
    API call to add a hostname for an environment
    """
    payload = {'site': uuid, 'path': 'environments/'+environment+'/hostnames/'+urllib.quote(hostname)}
    return api.request(session, payload, 'PUT')


def delete_hostname(session, uuid, environment, hostname):
    """
    API call to delete a hostname for an environment
    """
    payload = {'site': uuid, 'path': 'environments/'+environment+'/hostnames/'+urllib.quote(hostname)}
    return api.request(session, payload, 'DELETE')