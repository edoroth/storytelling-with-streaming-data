# Used code presented in lecture on 2/24/16
# Inserts whether edits were minor given information on bot

import json
import sys
import redis
import time
import urlparse

conn = redis.Redis(db=0)
conn1=redis.Redis(db=1)

while 1:
    line = sys.stdin.readline()
    try:
        d = json.loads(line)
    except ValueError:
        # sometimes we get an empty line, so just skip it
        continue

    try:
        bot = d["bot"]
    except KeyError:
        # if there is no city present in the message
        # then let's just ditch it
        continue

    try:
        minor = d["minor"]
    except KeyError:
        # if there is no referrer present in the message
        # then let's just ditch it
        continue

    if referrer == "direct":
        netloc = "direct"
    else:
        o = urlparse.urlparse(referrer)
        netloc = o.netloc

    conn.hincrby(city, netloc, 1)
    print json.dumps({"bot": bot, "minor": netloc})
    sys.stdout.flush()
