# Edo Roth (enr2116)
# Storytelling with Streaming Data Exercise 3
# This code builds an API that returns:
#   the rate of the stream coming from recent changes on Wikipedia entries as described in wikipedia_stream.py
#   the distributions assembled in wikipedia_distribution.py
#   the entropy of the distributions
#    the probability of a new wikipedia edit given the stored distributions
#
# Code modified from sample code presented in class


import flask
from flask import request
import redis
import collections
import json
import numpy as np

app = flask.Flask(__name__)
conn = redis.Redis(db=0)
conn1=redis.Redis(db=1)

def buildHistogram():
    keys = conn.keys()
    values = conn.mget(keys)
    c = collections.Counter(values)
    z = sum(c.values())
    return {k:v/float(z) for k,v in c.items()}

@app.route("/")
def histogram():
    h = buildHistogram()
    return json.dumps(h)

@app.route("/entropy")
def entropy():
    h = buildHistogram()
    return -sum([p*np.log(p) for p in h.values()]) 

@app.route("/probability")
def probability():
    city = request.args.get('city', '')
    ref = request.args.get('referrer', '')
    # get the distribution for the city
    print (city)
    d = conn.hgetall(city)
    # get the count for the referrer
    try:
      c = d[ref]
    except KeyError:
      return json.dumps({
        "city": city, 
        "prob": 0,
        "referrer": ref
      })
    # get the normalising constant
    z = sum([float(v) for v in d.values()])
    return json.dumps({
      "city": city, 
      "prob": float(c)/z,
      "referrer": ref
      })

    



if __name__ == "__main__":
    app.debug = True
    app.run()