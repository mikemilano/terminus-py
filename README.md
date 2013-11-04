Terminus Py
===========

This is a Python wrapper around the JSON API Pantheon exposes.

This is not meant to be a console app yet. Use Drush/Terminus for that.

Currently it manages the login session and wraps the Terminus API.

This example generates a session and retrieves the user's sites.

```
from terminus.api import api, user

session = api.auth('mikemilano@example.com', 'myawesomepassword')
sites = user.sites(session)
```

Take a look at terminus/api/* for all available methods.

### Roadmap

The plan is to add classes which are more abstracted from the API.

The goal would be to use the library like this:

```
# Note, the level higher than api here
from terminus import user, site

user = User('mikemilano@example.com', 'myawesomepassword')

# Access a site
my_awesome_site = user.sites('my_awesome_site')

# OR
all_sites = user.sites()
my_awesome_site = all_sites['my_awesome_site']

# Site level methods
# Get site info
info = my_awesome_site.info()

# Environment level methods:
# Not sure if environments should be an array of environment objects
# or if the environment should just be passed into the environment methods.

# So either
my_awesome_site.environments['dev'].lock('admin', 'password')

# OR
my_awesome_site.lock('dev', 'admin', 'password')
```


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