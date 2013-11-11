from api import user as userapi


class User:
    """
    Pantheon User
    """
    def __init__(self, session=None, attributes=None):
        """
        Constructs a Pantheon User object

        Args:
            session: requests.Session object for making API requests
            attributes: a dict of base attributes as returned from an API request
        """
        # Define attributes
        self.profile = {
            'firstname': None,
            'lastname': None,
            'created': None,
            'modified': None,
            'activity_level': None,
            'dashboard_visits': None,
            'maxdevsites': None,
            'devsites': None,
            'organization': None
        }
        self.uuid = None
        self.email = None
        self.keys = []
        self.sites = {}
        self.owned_sites = {}
        self.added = None
        self.organizations = None
        self.metadata = None
        # Set user object attributes
        self.session = session
        if attributes is not None:
            self._set_attributes(attributes)

    def _set_attributes(self, attributes):
        """
        Sets valid base level user object attributes from dict
        """
        for key, value in attributes.iteritems():
            key = key.replace('-', '_')
            if hasattr(self, key):
                setattr(self, key, value)

    def _set_profile_attributes(self, profile):
        """
        Sets profile level user object attributes from dict
        """
        for key, value in profile.iteritems():
            if key in self.profile:
                self.profile[key] = value

    def get_info(self):
        """
        Retrieves user attributes from the API and updates the user object
        """
        response = userapi.info(self.session)
        self._set_attributes(response)
        return response

    def get_profile(self):
        """
        Retrieves profile attributes from the API and updates the user object
        """
        response = userapi.profile(self.session)
        self._set_profile_attributes(response)
        return response

    def get_attribute(self, attribute):
        """
        Retrieves a single profile attribute from the API and updates the user object
        """
        if attribute in self.profile:
            response = userapi.attribute(self.session, attribute)
            self.profile[attribute] = response
            return response

    def set_attribute(self, attribute, value):
        """
        Sets a single profile attribute with the API and updates the user object
        """
        if attribute in self.profile:
            # Retrieve the value from the API and set local value based on the response
            try:
                response = userapi.attribute(self.session, attribute, value)
                self.profile[attribute] = response
                return response
            except ValueError:
                return

    def set_password(self, value):
        """
        Sets password with the API
        """
        try:
            response = userapi.password(self.session, value)
            if response.startswith('Set password for user'):
                return response
        except ValueError:
            pass
        return

    def get_email(self):
        """
        Retrieves email address from the API and updates the user object
        """
        response = userapi.email(self.session)
        self.email = response
        return response

    def set_email(self, value):
        """
        Sets email address with the API and updates the user object
        """
        try:
            response = userapi.email(self.session, value)
            self.email = value
            return response
        except ValueError:
            pass
        return False

    def delete(self):
        """
        Delete user account with the API
        """
        response = userapi.uuid(self.session)
        return response

    def get_keys(self):
        """
        Gets SSH keys from the API and updates the user object
        """
        response = userapi.keys(self.session)
        self.keys = response
        return response

    def add_key(self, key):
        """
        Adds a SSH key with the API and updates the user object
        """
        try:
            response = userapi.add_key(self.session, key)
            self.keys.append(key)
            return response
        except ValueError:
            pass
        return False

    def delete_key(self, key):
        """
        Removes a SSH key with the API and updates the user object
        """
        try:
            response = userapi.delete_key(self.session, key)
            self.keys.remove(key)
            return response
        except ValueError:
            pass
        return False

    def validate_key(self, key):
        """
        Validates SSH key with the API
        """
        try:
            response = userapi.validate_key(self.session, key)
            return response
        except ValueError:
            pass
        return False

    def get_uuid(self, email):
        """
        Gets a uuid of any user by email address from the API
        """
        response = userapi.uuid(self.session, email)
        return response

    def get_email_by_email(self, email):
        """
        ...
        """
        response = userapi.check_email_by_email(self.session, email)
        return response

    def get_sites(self):
        """
        Retrieves sites from the API and updates the user object
        """
        response = userapi.sites(self.session)
        self.sites = {}
        for uuid, site in response.iteritems():
            site['uuid'] = uuid
            self.sites[site['name']] = site
        return response

    def get_owned_sites(self):
        """
        Retrieves owned sites from the API and updates the user object
        """
        response = userapi.owned_sites(self.session)
        self.owned_sites = {}
        for uuid, site in response.iteritems():
            site['uuid'] = uuid
            self.owned_sites[site['name']] = site
        return response
