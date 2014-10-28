__author__ = 'Steph'

import couchdb

#manually set database location
gs_database_url = "https://frchelpertest.iriscouch.com"

#manually set database name
db_name = "data"

#manually set document id values
rankings_id = "rankings"
schedule_id = "schedule"
next_match_id = "next_match"

#connect to server
db = couchdb.Server(gs_database_url)

#get initial document rev numbers
rankings_rev = db[db_name].get(rankings_id).rev
schedule_rev = db[db_name].get(schedule_id).rev
next_match_rev = db[db_name].get(next_match_id).rev