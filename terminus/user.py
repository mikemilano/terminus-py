import api


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
            kwargs: data from the API
        """
        # Define properties
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
        self.added = None
        self.organizations = None
        self.email = None
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

