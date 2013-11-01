import api


def log(session, uuid):
    payload = {'site': uuid, 'path': 'code-log'}
    return api.request(session, payload)


def upstream(session, uuid, updatedb=False, overwrite=False):
    payload = {'site': uuid, 'path': 'code-upstream-updates'}
    if not updatedb:
        return api.request(session, payload)
    else:
        if overwrite:
            xoption = 'theirs'
        else:
            xoption = ''
        data = {'updatedb': updatedb, 'xoption': xoption}
        return api.request(session, payload, 'POST', data)