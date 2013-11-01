import api


def clone_database(session, uuid, source, target, updatedb=False):
    """
    API call to clone a database between site environments
    """
    payload = {'site': uuid, 'path': 'environments/'+target+'/database'}
    data = {
        'clone-from-environment': source,
        'updatedb': 1 if updatedb else 0
    }
    return api.request(session, payload, 'POST', data)


def clone_files(session, uuid, source, target):
    """
    API call to clone user files between site environments
    """
    payload = {'site': uuid, 'path': 'environments/'+target+'/files'}
    data = {
        'clone-from-environment': source,
    }
    return api.request(session, payload, 'POST', data)


def clone_code(session, uuid, environment, updatedb=False):
    """
    API Function to deploy code to a site environment
    """
    payload = {'site': uuid, 'path': 'environments/'+environment+'/code'}
    data = {
        'updatedb': 1 if updatedb else 0
    }
    return api.request(session, payload, 'POST', data)


def wipe(session, uuid, environment):
    """
    API Function to Wipe an Environment
    """
    payload = {'site': uuid, 'path': 'environments/'+environment+'/wipe'}
    return api.request(session, payload, 'POST')