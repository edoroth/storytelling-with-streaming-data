#!/bin/bash
# Author: Edo Roth (enr2116)
# 2/24/16

# Script to run all three python scripts for Exercise 2
# Code creates a stream of data from Wikipedia API, calculates its rate, and alerts an uptake
# in 2016 U.S. Presidential Candidate Wikipedia edits via tweetbot at @dropshot_lob
# Standard output from each program is fed into subsequent standard input of the following script
python wikipedia_stream_2.py | python wikipedia_diff.py | python wikipedia_tweet.py