# Author: Edo Roth
# Storytelling with Streaming Data
# Code for submission for Exercise 3
# Modified code from code provided in lecture on 2/10/16, 
# as well as from submission from exercise 2

# Monitors the rate of Wikipedia edits made by software bots by grouping into buckets of 10 edits at a time

import json
import sys

last = 0
# Create empty lists to store most recent differences and most recent edits
diffs = []
edits = []

# Run forever to ensure we continually get all messages and constantly measure rate
while 1:
	# Get output of previous program which is pumped in through standard input
    line = sys.stdin.readline()
    # Parse JSON format
    d = json.loads(line)
    # Get
    if last == 0 :
        last = d["t"]
        continue
    delta = d["t"] - last
    # We calculate the rate by averaging over 3 edits at a time
    # As long as we haven't seen 10 edits, we stored the time differences and edits themselves
    if (len(diffs) < 10 and d["bot"] == "yes"):
    	diffs.append(delta)
    	edits.append(d)
    	# Write to standard error when an edit is made to monitor all edits going on
    	sys.stderr.write(d["name"])
    # We measure the rate over an average of 3 total differences. This gives us an average rate for our stream.
    # I chose ten because this is a good indication of noticeable activity by bots
    if (len(diffs) == 10):
    	# Calculate rate by summing all differences over the last 3 differences seen
    	rate = sum(diffs)/float(len(diffs))
    	# Write to standard error every ten edits to keep track of rate
    	sys.stderr.write("rate is" + str(rate))
    	if (rate < 30.00):
    		s = ""
    		i = 0
    		# Formatting to print out the names of the most recent articles edited.
    		# I chose to print the names of the individual articles edited, so that
    		# when we get an uptick in rate, we can notify the specific articles edited
    		# as evidence of activity -- this may give some insight on the reasons for
    		# some of these relatively high-paced changes
    		for	edit in edits:
    			if (i != len(edits)-1):
    				s = s + edit["name"] +  ", "
    			else:
    				s = s + edit["name"] + "."
    			i = i + 1
    		# Printing out one line for ease of converting an alert to a tweet
    		print (s)
    		sys.stdout.flush()

    	# Reset lists to begin a new rate counter	
    	diffs = []
    	edits = []

    last = d["t"]





