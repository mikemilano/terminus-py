Pantheon Terminus Python Library
================================

This is largely a work in progress, but here is
and example of the the usage I'm shooting for.

```
# Validate and create a session
account = terminus.auth('mmilano@example.com', 'myawesomepassword')

# Get a dict of sites
sites = account.sites()

# Get a single site
myawesomesite = account.sites('myawesomesite')

# Lock (add http password) to myawesomesite dev
myawesomesite.lock('dev', 'myhttpusername', 'myhttppassword')
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