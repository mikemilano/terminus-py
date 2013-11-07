from api import api, \
    user as userapi
from user import User
from site import Site


class Session:
    """
    Terminus session
    """
    def __init__(self, email=None, password=None):
        """
        Instantiates a terminus session object
        """
        self.session = None
        """ requests.session object used for API calls """
        self.email = email
        """ Email address of the session owner """
        self.password = password
        """ Password of the session owner """
        self.uuid = None
        """ uuid of the session owner """
        self.user = None
        """ User object of the session owner """
        self.sites = None
        """ A dict of site objects keyed by site name """
        self.sitemap = None
        """ A dict of site names keyed by site uuid """
        if email is not None and password is not None:
            self.auth()

    def auth(self):
        """
        Authenticates against the API and sets the self.user object
        """
        self.session = api.auth(self.email, self.password)
        self.uuid = self.session.cookies.get('uuid')
        # Set user object
        properties = userapi.info(self.session)
        properties['uuid'] = self.uuid
        self.user = User(self.session, properties)
        self.load_sites()

    def load_sites(self):
        """
        Sets self.sites as a dict of site objects, keyed by site name
        """
        sites = userapi.sites(self.session)
        self.sites = {}
        for uuid, properties in sites.iteritems():
            properties['uuid'] = uuid
            name = properties['information']['name']
            self.sites[name] = Site(properties)
            self.sitemap[uuid] = name
