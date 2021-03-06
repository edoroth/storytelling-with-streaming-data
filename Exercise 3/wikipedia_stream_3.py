#Author: Edo Roth
#Storytelling with Streaming Data
#Code for submission for Exercise 3, modified from submission from Exercises 1 and 2
#3/12/16

#!/usr/bin/env python
import requests
import json
import time
import codecs
from sys import stdout
from sys import stderr

''' Function to remove all non-ASCII characters
Wikipedia contains many articles with non-ASCII characters in their titles
and for the purpose of this project these are not meaningful, as all candidates
have only ASCII characters in their names'''
def checkstring(s):
    good_chars = (c for c in s if 0 < ord(c) < 127)
    return ''.join(good_chars)

# Creating blank dictionary to keep track of logged edits (and not print duplicates
# if request returns same entry twice)
# 
# It's important that every single edit is marked as a separate entry, so we keep track
# of a dictionary which is indexed by revision id. Wikipedia guaranteed unique revision
# identificication numbers for every unique edit which we use for this purpose.
logged_edits = {}

# Run forever
# Ensures that this continues to gather information for as long as the service is running
while True:

    # Send request to Wikipedia API (will get 100 changes at a time)
    # I chose to receive the following information:
    #   -Revision ID
    #   -Title of Article
    #   -Timestamp of Article's edit
    #   -Flags containing information on whether article was edited by a bot, a minor edit, or a new page
    # All of this information is essential to verify that we are dealing with unique edits, and to extract information about the articles being edited
    s = requests.get('https://en.wikipedia.org/w/api.php?action=query&list=recentchanges&format=json&rcprop=ids|title|timestamp|flags&rclimit=100')

    # Check status code to ensure good response
    # If any code other than 200 is received, the program may crash and I wanted a tool to understand the failure.
    # This error will likely arise only from server error, as the request is properly formatted.
    if (s.status_code != 200):
        print ("ERROR: STATUS CODE OTHER THAN 200")

    # Parse into JSON format
    # Wikipedia provides data in a JSON format and this is a useful format for us to use
    j = s.json()

    #Get list of all recent changes by using appropriate JSON tags
    all_changes = j["query"]["recentchanges"]

    # Go through all changes in received by request
    # We want to comb through all recent changes to ensure we cover all edits that have been made while the program runs
    for change in all_changes:

        # Check if entry has already been encountered by checking its revision ID
        # If the entry has not been seen, we add it to our dictionary to mark it
        if change["revid"] not in logged_edits:
            logged_edits[change["revid"]] = change["revid"]

            # Get rid of category and talk pages
            # The colon only appears in titles when they are not main articles pages.
            # As a study of articles about candidates, and the way that they are used to convey information to the public,
            # I chose to ignore category and talk pages because they are more internally-facing articles and thus don't 
            # reflect edits meant for view by the wider public
            if  ":" not in change["title"] :

                # Print the title of the article that was edited along with the current time
                # Prints four different categories for whether edits were made by a bot or not and whether they were
                # 'minor' edits as determined by Wikipedia
                # This allows every single edit to be logged individually when it comes in.
                if 'bot' in change and 'minor' in change:
                    print (json.dumps({"t": time.time(), "name": checkstring(change["title"]), "bot": "yes", "minor":"yes"}))
                if 'bot' in change and 'minor' not in change:
                    print (json.dumps({"t": time.time(), "name": checkstring(change["title"]), "bot": "yes", "minor":"no"}))
                if 'bot' not in change and 'minor' in change:
                    print (json.dumps({"t": time.time(), "name": checkstring(change["title"]), "bot": "no", "minor":"yes"}))
                if 'bot' not in change and 'minor' not in change:
                    print (json.dumps({"t": time.time(), "name": checkstring(change["title"]), "bot": "no", "minor":"no"}))

        #Empty the buffer
        stdout.flush()
        #jstderr.flush()

    # Wait before next request.
    # Waiting for 5 seconds before sending a request means that we have a margin of error of 5 seconds in marking the time difference
    # between edits. However, as we deem a string of 3 messages coming every 2 minutes as significant, this margin is insignificant.
    time.sleep(5)