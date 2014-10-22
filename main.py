#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import cgi
import webapp2
from urllib2 import Request, urlopen
import json

MAIN_PAGE_HTML = """\
<html>
  <body>
    <form action="/EventListing" method="post">
      <div><textarea name="content" rows="3" cols="60"></textarea></div>
      <div><input type="submit" value="Get CMP"></div>
    </form>
  </body>
</html>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_HTML)

class FRCEventListingRequest(webapp2.RequestHandler):
    def post(self):
        request = Request("http://private-anon-f696a1583-frceventsprelim.apiary-mock.com/2014/events?eventCode=CMP&districtCode=PNW&excludeDistrict=true")
        Request.add_header(request, "Accept", "application/json")
        Request.add_header(request, "Authorization", "Token communitysampletoken")
        response_body = urlopen(request).read()
        self.response.write('<html><body>Response:<pre>')
        self.response.write(cgi.escape(response_body))
        self.response.write('</pre></body></html>')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/EventListing', FRCEventListingRequest),
], debug=True)
