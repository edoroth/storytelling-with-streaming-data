#Author: Edo Roth
#Storytelling with Streaming Data
#2/9/16

#!/usr/bin/env python
import requests
import json
import time
import codecs
from sys import stdout

''' Function to remove all non-ASCII characters'''
def checkstring(s):
    good_chars = (c for c in s if 0 < ord(c) < 127)
    return ''.join(good_chars)

#Creating blank dictionary to keep track of logged edits (and not print duplicates
#if request returns same entry twice)
logged_edits = {}

#Run forever
while True:

    #Send request to Wikipedia API (will get 10 changes at a time)
    s = requests.get('https://en.wikipedia.org/w/api.php?action=query&list=recentchanges&format=json&rcprop=ids|title|user|timestamp&rclimit=10')

    #Check status code to ensure good response
    if (s.status_code != 200):
        print ("UH OH")

    #Parse into JSON format
    j = s.json()

    #Get list of changes
    all_changes = j["query"]["recentchanges"]

    #Go through all changes in received by request
    for change in all_changes:

        #Check if entry has already been encountered
        if change["revid"] not in logged_edits:
            logged_edits[change["revid"]] = change["revid"]

            #Get rid of category and talk pages -- only using articles
            if  ":" not in change["title"] :
                #Get specific user details with additional API request
                this_user = requests.get('https://en.wikipedia.org/w/api.php?action=query&list=users&ususers=' + change["user"] + '&format=json&usprop=editcount')
                user = this_user.json()
                #Get rid of anonymous users by ensuring that an edit count exists
                if ('editcount' in user["query"]["users"][0]):
                    #Print output to stdout
                    print (checkstring(change["title"]) + " was edited by " + checkstring(change["user"])  +" who has "+ str(user["query"]["users"][0]["editcount"])+" edits")
        #Empty the buffer
        stdout.flush()

    #Wait before next request
    time.sleep(1)