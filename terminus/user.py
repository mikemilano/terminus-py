from api import api, \
    user as userapi

class User:
    """
    Pantheon User
    """
    def __init__(self, session=None, properties=None):
        """
        Constructs a Pantheon User object

        Args:
            session: requests.Session object for making API requests
            uuid: User's uuid
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
        self.added = None
        self.organizations = None
        self.metadata = None
        # Set properties
        self.session = session
        if properties is not None:
            self.set_properties(properties)

    def set_properties(self, properties):
        """
        Sets valid properties from dict
        """
        for key, value in properties.iteritems():
            key = key.replace('-', '_')
            if hasattr(self, key):
                setattr(self, key, value)

    def load(self):
        """
        Loads user attributes from the API into this user object
        """
        self.set_properties(userapi.info(self.session))

    def attr(self, attribute, value=None):
        """
        Gets/sets profile attribute using the API.
        """
        if attribute in self.profile:
            if value is None:
                # Retrieve the value from the API and set local value based on the response
                try:
                    response = userapi.attribute(self.session, attribute, value)
                    self.profile[attribute] = response
                except ValueError:
                    return False
            else:
                # Set the value with the API and set the local value with a successful return
                try:
                    response = userapi.attribute(self.session, attribute, value)
                    if response.startswith('Set profile field'):
                        self.profile[attribute] = value
                        return True
                except ValueError:
                    return False

    def password(self, value):
        """
        Sets password and returns True upson success
        """
        try:
            response = userapi.password(self.session, value)
            if response.startswith('Set password for user'):
                return True
            else:
                return False
        except ValueError:
            return False
