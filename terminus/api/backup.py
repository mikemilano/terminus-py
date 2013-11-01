import api
import time


def catalog(session, uuid, environment):
    """
    API call to get the backup catalog
    """
    payload = {'site': uuid, 'path': 'environments/'+environment+'/backups/catalog'}
    return api.request(session, payload)


def download_url(session, uuid, environment, bucket, element):
    """
    API call to get a single backup item's S3 token
    """
    payload = {
        'site': uuid,
        'path': 'environments/'+environment+'/backups/catalog/'+bucket+'/'+element+'/s3token'
    }
    return api.request(session, payload)


def backup(session, uuid, environment, entry_type, code=True, db=True, files=True):
    """
    API Function to make a backup
    """
    payload = {'site': uuid, 'path': 'environments/'+environment+'/backups/create'}
    data = {
        'entry_type': entry_type,
        'scheduled_for': int(time.time()),
        'code': 1 if code else 0,
        'database': 1 if db else 0,
        'files': 1 if files else 0
    }
    return api.request(session, payload, 'POST', data)