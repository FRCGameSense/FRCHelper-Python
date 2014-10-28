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
import GsDatabaseSettings as database
import json
import logging

MAIN_PAGE_HTML = """\
<html>
    <body>
        <form action="/Rankings/Data" method="post">
            <div><textarea name="event" rows="3" cols="60"></textarea></div>
            <div><input type="submit" value="Get Rankings"></div>
        </form>
        <form action="/NextMatch/Data" method="post">
            <div><textarea name="event" rows="3" cols="60"></textarea></div>
            <div><textarea name="match_num" rows="3" cols="60"></textarea></div>
            <div><input type="submit" value="Next Match"></div>
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
        event = cgi.escape(self.request.get('event'))
        rankings = communicator.get_rankings(2014, event)
        rankings_json = [{'Rankings': rankings.to_string}]
        self.response.write(json.dumps(rankings_json))
        database.rankings_id, database.rankings_rev = database.db[database.db_name].save({
            "_id": database.rankings_id,
            "_rev": database.rankings_rev,
            "rankings": rankings.to_string
        })


class FrcNextMatchRequestHandler(webapp2.RedirectHandler):
    def post(self):
        event = cgi.escape(self.request.get('event'))
        schedule_response = communicator.get_schedule(2014, event, "qual")
        match_num = int(cgi.escape(self.request.get('match_num')))
        for match in schedule_response.schedule:
            if match.match_number == match_num:
                self.response.write(match.to_json())
                database.next_match_id, database.next_match_rev = database.db[database.db_name].save({
                    "_id": database.next_match_id,
                    "_rev": database.next_match_rev,
                    "next_match": match.to_json(),
                })



app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/EventListing/Data', FrcEventListingRequestHandler),
    ('/Rankings/Data', FrcRankingsRequestHandler),
    ('/NextMatch/Data', FrcNextMatchRequestHandler),
], debug=True)
