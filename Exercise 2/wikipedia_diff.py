#Author: Edo Roth
#Storytelling with Streaming Data
#Code for submission for Exercise 2
#2/24/16


import json
import sys
import redis


last = 0
diffs = []
while 1:
    line = sys.stdin.readline()
    d = json.loads(line)
    if last == 0 :
        last = d["t"]
        continue
    delta = d["t"] - last
    #print (json.dumps({"delta":delta, "t":d["t"]}))
    #We calculate the rate by looking at 10 messages a time
    if (len(diffs) < 10):
    	diffs.append(delta)
    if (len(diffs) == 10):
    	rate = sum(diffs)/float(len(diffs))
    	print ("rate is %.3f seconds per message" % rate )
    	if (rate < 0.500):
    		print ("Holy smokes we've got some activity!")
    	diffs = []
    sys.stdout.flush()
    last = d["t"]





