Terminus Py
===========

This is a Python wrapper around the JSON API Pantheon exposes.

This is not meant to be a console app yet. Use Drush/Terminus for that.

## Usage
```
from terminus.session import Session
s = Session('mikemilano@example.com', 'myawesomepassword')

# s.user is a terminus.user object for the authenticated user
#
# Example: set password
s.user.set_password('mynewpassword')

# The site class is incomplete, but here is some information:
#
# s.sites is a dict of terminus.site objects, keyed by site name
#
# Example: Set service level
s.sites['myawesomesite'].set_service_level('basic')

# The environments class is incomplete
#
# s.sites['myawesomesite'].environments is a dict of terminus.environment
# objects keyed by environment name. (dev, test, live, and multidev names)
#
# Example: Lock environment
s.sites['myawesomesite'].environments['dev'].lock('admin', 'secretpassword')
```

### API usage for terminus.api modules

The API modules are what the higher level classes use to communicate
to the API. You can use these directly as well.
```
from terminus.api import api, user

# Set 'sites' to a dict of user sites, as returned by the API
session = api.auth('mikemilano@example.com', 'myawesomepassword')
sites = user.sites(session)
```

Take a look at terminus/api/* for all available methods.

### Roadmap

The plan is to finish out the higher level classes
which are more abstracted from the API.


### MIT license

Copyright (c) 2013 Mike Milano.

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.