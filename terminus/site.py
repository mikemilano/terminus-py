from environment import Environment
from api import site as siteapi


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
        Sets valid properties from dict. This data is returned from
        various site API calls such as: info, settings, & state.

        If pre-defined key names (site, information) hold nested property data,
        then values within those dicts will be set accordingly.
        """
        if properties is None:
            return

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

    def load_info(self):
        """
        Loads and returns site info data from API
        """
        response = siteapi.info(self.session, self.uuid)
        self.set_properties(response)
        return response

    def load_state(self):
        """
        Loads and returns state data from API
        """
        response = siteapi.state(self.session, self.uuid)
        self.set_properties(response)
        return response

    def delete(self):
        """
        Deletes the site
        """
        siteapi.delete(self.session)

    def settings(self):
        """"
        Loads and returns settings data from API
        """
        response = siteapi.settings(self.session, self.uuid)
        self.set_properties(response)
        return response

    def service_level(self, level=None):
        """
        Loads and returns service level if level is not set.
        If the level argument is passed in, it is set.
        """
        response = siteapi.settings(self.session, self.uuid, level)
        self.service_level = response
        return response
