#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Edo Roth
#Storytelling with Streaming Data
#Exercise 3 

# Twitter bot that takes information about a spike in the rate of articles edited on Wikipedia by software bots.
# Will send a tweet to the account @dropshot_lob every time it receives information -- should be used conjunctively
# with wikipedia_diff_3.py for correct input information

import tweepy
import sys

# Information for specific twitter account
auth = tweepy.OAuthHandler('gK7fQYGphcBgItj2SpKnDoyps', 'VhhhSW8cpN4KPgj42z8UGvvZocvgXnI4MndE7Qkv0VMTHankaX')
auth.set_access_token('1053424819-7WjwCzB45PjigGOLDz7en7eZR1Ps6S7ir8KV2eM', 'Xa1Z67zauYMuJYxPFzvzgtHR2cebs9OXU4UnmPEXJDaXQ')

# Connecting to the API which allows posts
api = tweepy.API(auth)

# Get line from standard input, which will be the output of the piped articles coming from our stream rate calculator
line = sys.stdin.readline()

# Send out tweet -- tweets are limited to 140 characters, so if the names of the articles happen to be long, they will be truncated.
api.update_status("Wikipedia bots are making some intense edits!")
