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
import GsFrcApiCommunicator as communicator
import json

MAIN_PAGE_HTML = """\
<html>
    <body>
        <form action="/EventListing/Data" method="post">
            <div><input type="submit" value="Get Event"></div>
        </form>
        <form action="/Rankings/Data" method="post">
            <div><input type="submit" value="Get Rankings"></div>
        </form>
    </body>
</html>
"""


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_HTML)


class FrcEventListingRequestHandler(webapp2.RequestHandler):
    def post(self):
        event_listing = communicator.get_event_listing(2014, "ILIL")
        self.response.write('<html><body>Response:<pre>')
        self.response.write(event_listing.events_list[0].name)
        self.response.write('</pre></body></html>')


class FrcRankingsRequestHandler(webapp2.RequestHandler):
    def post(self):
        rankings = communicator.get_rankings(2014, "ILIL")
        rankings_json = [{'Rankings': rankings.to_string}]
        self.response.write(json.dumps(rankings_json))


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/EventListing/Data', FrcEventListingRequestHandler),
    ('/Rankings/Data', FrcRankingsRequestHandler),
], debug=True)
