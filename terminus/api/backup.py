import api
import time


def catalog(session, uuid, environment):
    payload = {'site': uuid, 'path': 'environments/'+environment+'/backups/catalog'}
    return api.request(session, payload)


def download_url(session, uuid, environment, bucket, element):
    payload = {
        'site': uuid,
        'path': 'environments/'+environment+'/backups/catalog/'+bucket+'/'+element+'/s3token'
    }
    return api.request(session, payload)


def backup(session, uuid, environment, entry_type, code=True, db=True, files=True):
    payload = {'site': uuid, 'path': 'environments/'+environment+'/backups/create'}
    data = {
        'entry_type': entry_type,
        'scheduled_for': int(time.time()),
        'code': 1 if code else 0,
        'database': 1 if db else 0,
        'files': 1 if files else 0
    }
    return api.request(session, payload, 'POST', data)