# Edo Roth (enr2116)
# 3/12/16
# Storytelling with Streaming Data Exercise 3
# This code builds an API that returns:
#   the rate of the stream coming from recent changes on Wikipedia entries as described in wikipedia_stream.py:
#       this rate specifically monitors the rate of Wikipedia edits made by software bots
#   the distributions assembled from Wikpedia edits
#       splits data into four categories categorized by whether or not edits were made by bots and whether they were minor
#       we look at these two variables and treat them similarly to city and referrer in the in-class example, although we 
#       have a far more limited possible set of values in this case.
#   the entropy of the distributions
#   the probability of a new wikipedia edit given the stored distributions
#
#
#
# Code modified from code presented in lecture on 2/24/16

#Importing all modules required
import flask
from flask import request
import redis
import collections
import json
import numpy as np

#Creates flask app
app = flask.Flask(__name__)
conn = redis.Redis(db=0)
conn1=redis.Redis(db=1)

# Grabs the elements from Redis and builds a histogram for the different categories
def buildHistogram():
    keys = conn.keys()
    values = conn.mget(keys)
    c = collections.Counter(values)
    z = sum(c.values())
    return {k:v/float(z) for k,v in c.items()}

# Creates the website at localhost:5000/distributions
@app.route("/distributions")
def histogram():
    h = buildHistogram()
    return json.dumps(h)

@app.route("/rate")
def rate():
  return "0"

@app.route("/entropy")
def entropy():
    h = buildHistogram()
    return -sum([p*np.log(p) for p in h.values()]) 

@app.route("/probability")
def probability():
    bot = request.args.get('bot', '')
    minor = request.args.get('minor', '')
    # get the distribution for the bot on whether edits were minor or not
    print bot
    d = conn.hgetall(bot)
    # get the count for number of minor edits
    try:
      c = d[minor]
    except KeyError:
      return json.dumps({
        "bot": bot, 
        "prob": 0,
        "minor": minor
      })
    # get the normalising constant
    z = sum([float(v) for v in d.values()])
    return json.dumps({
      "bot": bot, 
      "prob": float(c)/z,
      "minor": minor
      })


if __name__ == "__main__":
    app.debug = True
    app.run()