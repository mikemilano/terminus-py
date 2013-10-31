import terminus


class Site:
    def __init__(self, session, uuid):
        self.session = session
        self.uuid = uuid

        # Default environments
        self.environments = {
            'dev': self.default_environment(),
            'test': self.default_environment(),
            'live': self.default_environment()
        }

        # API vars
        self.utm_campaign = None
        self.service_level = None
        self.name = None
        self.creator = None
        self.created_at = None
        self.created = 0
        self.utm_source = None
        self.instrument = None
        self.upstream = {'url': None, 'branch': None},
        self.owner = None
        self.organization = None
        self.preferred_zone = None

    def default_environment(self):
        return {
            'diffstat': {},
            'environment_created': 0,
            'on_server_development': False,
            'lock': {'username': None, 'password': None, 'locked': False}
        }

    # API Calls
    def info(self):
        payload = {'site': self.uuid, 'path': ''}
        response = self.session.get(terminus.TURL, params=payload)
        return terminus.handle_response(response)

    def state(self):
        payload = {'site': self.uuid, 'path': 'state'}
        response = self.session.get(terminus.TURL, params=payload)
        return terminus.handle_response(response)

    def delete(self):
        return None

    def settings(self):
        payload = {'site': self.uuid, 'path': 'settings'}
        response = self.session.get(terminus.TURL, params=payload)
        return terminus.handle_response(response)

    def get_service_level(self):
        payload = {'site': self.uuid, 'path': 'service-level'}
        response = self.session.get(terminus.TURL, params=payload)
        return terminus.handle_response(response)

    def set_service_level(self, service_level):
        return None

    def get_attribute(self, attribute):
        payload = {'site': self.uuid, 'path': 'attributes/'+attribute}
        response = self.session.get(terminus.TURL, params=payload)
        return terminus.handle_response(response)

    def set_attribute(self, attribute, value):
        return None

    def get_attributes(self):
        payload = {'site': self.uuid, 'path': 'attributes'}
        response = self.session.get(terminus.TURL, params=payload)
        return terminus.handle_response(response)

    def set_attributes(self, attributes):
        return None

    def delete_attributes(self):
        return None

    def get_upstream(self):
        payload = {'site': self.uuid, 'path': 'code-upstream'}
        response = self.session.get(terminus.TURL, params=payload)
        return terminus.handle_response(response)

    def get_team_members(self):
        payload = {'site': self.uuid, 'path': 'team'}
        response = self.session.get(terminus.TURL, params=payload)
        return terminus.handle_response(response)

    def delete_team_member(self, uuid):
        return None

    def invite_team_member(self, email, invited_by):
        return None

    def verify_team_member(self, uid):
        return None

    def get_owner(self):
        payload = {'site': self.uuid, 'path': 'owner'}
        response = self.session.get(terminus.TURL, params=payload)
        return terminus.handle_response(response)

    def screenshot(self):
        return None

    def events(self, environment, limit=100):
        payload = {'site': self.uuid, 'path': 'environments/'+environment+'?limit='+limit}
        response = self.session.get(terminus.TURL, params=payload)
        return terminus.handle_response(response)

    def get_binding(self, environment, type):
        payload = {'site': self.uuid, 'path': 'environment/'+environment+'/bindings?type='+type}
        response = self.session.get(terminus.TURL, params=payload)
        return terminus.handle_response(response)

    def get_bindings(self, environment):
        payload = {'site': self.uuid, 'path': 'environment/'+environment+'/bindings'}
        response = self.session.get(terminus.TURL, params=payload)
        return terminus.handle_response(response)

    def clear_cache(self, environment):
        return None

    def get_onserver_status(self, environment):
        payload = {'site': self.uuid, 'path': 'environments/'+environment+'/on-server-development'}
        response = self.session.get(terminus.TURL, params=payload)
        return terminus.handle_response(response)

    def set_onserver_status(self, environment, status):
        return None

    def commit(self, environment, message, uuid):
        return None

    def diff(self, environment, filepath):
        payload = {'site': self.uuid, 'path': 'environments/'+environment+'/on-server-development/diffstat'}
        response = self.session.get(terminus.TURL, params=payload)
        return terminus.handle_response(response)

    def diff_stats(self, environment):
        return None

    def lock(self, environment, username, password):
        return None

    def delete_lock(self, environment):
        return None

    def hostnames(self, environment):
        payload = {'site': self.uuid, 'path': 'environments/'+environment+'/hostnames'}
        response = self.session.get(terminus.TURL, params=payload)
        return terminus.handle_response(response)

    def add_hostname(self, environment, hostname):
        return None

    def delete_hostname(self, environment, hostname):
        return None

    def environments(self):
        payload = {'site': self.uuid, 'path': 'environments'}
        response = self.session.get(terminus.TURL, params=payload)
        return terminus.handle_response(response)

    def notifications(self):
        payload = {'site': self.uuid, 'path': 'notifications'}
        response = self.session.get(terminus.TURL, params=payload)
        return terminus.handle_response(response)

    def bindings(self):
        payload = {'site': self.uuid, 'path': 'bindings'}
        response = self.session.get(terminus.TURL, params=payload)
        return terminus.handle_response(response)