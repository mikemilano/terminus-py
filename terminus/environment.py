from api import api


class Environment:
    def __init__(self, session=None, properties=None):
        """
        Instantiates an environment object.

        kwargs data is data returned from the API.api

        api.site.environments() returns a light set of environment data
        api.site.state() returns much more detail about each environment
        """
        # Define properties
        self.urls = None
        self.dbserver = None
        self.allow_domains = None
        self.lock = None
        self.max_num_cdes = None
        self.site = None
        self.schedule = None
        self.nginx = None
        self.min_backups = None
        self.mysql = None
        self.owner = None
        self.preferred_zone = None
        self.failover_appserver = None
        self.errors = None
        self.name = None
        self.environment_created = None
        self.php_fpm = None
        self.redis = None
        self.environment = None
        self.appserver = None
        self.allow_read_slaves = None
        self.statuses = None
        self.maintenance = None
        self.max_backups = None
        self.allow_cacheserver = None
        self.ssl_enabled = None
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