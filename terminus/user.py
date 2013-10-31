import terminus

class User:
    """
    Pantheon User
    """
    def __init__(self, session, uuid):
        """
        Constructs a Pantheon User object

        Args:
            session: requests.Session object for making API requests
            uuid: User's uuid
            email: User's email
        """
        self.session = session
        self.realm = 'user'
        self.uuid = uuid

    def get_user(self):
        payload = {'user': self.uuid, 'path': ''}
        response = self.session.get(terminus.TURL, params=payload)
        return terminus.handle_response(response)

    def get_profile(self):
        payload = {'user': self.uuid, 'path': 'profile'}
        response = self.session.get(terminus.TURL, params=payload)
        return terminus.handle_response(response)

    def set_profile(self, profile):
        return None

    def update_profile(self, profile):
        return None

    def get_attribute(self, attribute):
        payload = {'user': self.uuid, 'path': 'profile/'+attribute}
        response = self.session.get(terminus.TURL, params=payload)
        return terminus.handle_response(response)

    def set_attribute(self, attribute):
        return None

    def set_password(self, password):
        return None

    def get_email(self):
        payload = {'user': self.uuid, 'path': 'email'}
        response = self.session.get(terminus.TURL, params=payload)
        return terminus.handle_response(response)

    def set_email(self, email):
        return None

    def get_uuid(self, email):
        return None

    def get_email_by_email(self, email):
        return None

    def delete(self):
        return None

    def get_keys(self):
        payload = {'user': self.uuid, 'path': 'keys'}
        response = self.session.get(terminus.TURL, params=payload)
        return terminus.handle_response(response)

    def add_key(self, key):
        return None

    def delete_keys(self):
        return None

    def validate_key(self, key):
        return None

    def sites(self):
        payload = {'user': self.uuid, 'path': 'sites'}
        response = self.session.get(terminus.TURL, params=payload)
        return terminus.handle_response(response)

    def owned_sites(self):
        payload = {'user': self.uuid, 'path': 'sites?owned=1'}
        response = self.session.get(terminus.TURL, params=payload)
        return terminus.handle_response(response)


class Profile:
    def __init__(self):
        self.firstname = None
        self.created = None
        self.lastname = None
        self.invited_by = None
        self.modified = None
        self.invited_to = None
        self.activity_level = None
        self.dashboard_visits = []
        self.maxdevsites = None
        self.verify = None
        self.organization = None
        self.screen_intro_multidev_module = None

