from environment import Environment


class Site:
    def __init__(self, session=None, properties=None):
        """
        Instantiates a site object.

        The goal is to support instantiating a site from various data structures return by the API.

        user.sites() holds site properties in response['information']
        site.state() holds site properties in response['site']

        """
        # Define properties
        # Site properties available in: api.site.info()
        self.uuid = None
        self.name = None
        self.service_level = None
        self.created = None
        self.created_at = None
        self.owner = None
        self.preferred_zone = None
        # Additional site properties available in: api.user.sites()
        self.upstream = {
            'url': None,
            'branch': None
        }
        # Additional site properties available in: api.site.state()
        self.settings = None
        self.base_domain = None
        self.environments = {}
        self.instrument = {
            'billing_hash': None,
            'subscription_uuid': None,
            'label': None,
            'instrument': None,
            'user': None,
            'last_confirmed': None,
            'dirty': None
        }
        self.add_ons = None
        self.user = None
        self.team = None
        self.organization = None
        self.jobs = None
        # Set properties
        self.session = session
        self.base_keys = ['site', 'information']

        if properties is not None:
            self.set_properties(properties)

    def set_properties(self, properties):
        """
        Sets valid properties from dict.
        If pre-defined key names (site, information) hold nested property data,
        then values within those dicts will be set accordingly.
        """
        # Setup environments
        if 'environments' in properties:
            for name, env_properties in properties['environments'].iteritems():
                env_properties['name'] = name
                self.environments[name] = Environment(self.session, env_properties)
            properties.pop('environments', None)

        # Populate the rest of the properties
        for key, value in properties.iteritems():
            key = key.replace('-', '_')
            if hasattr(self, key):
                setattr(self, key, value)
            if key in self.base_keys:
                self.set_properties(value)
