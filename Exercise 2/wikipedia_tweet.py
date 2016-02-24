#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Edo Roth
#Storytelling with Streaming Data
#Exercise 2

# Twitter bot that takes information about a spike in the rate of articles edited on Wikipedia about 2016 Presidential candidates.
# An uptake in rate (3 edits in less than 2 minutes) will cause a tweet to be sent, containing the names of those articles.

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
api.update_status("Candidate Wikipedia articles are being edited: " + line[0:min(93,len(line))])
