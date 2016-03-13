Edo Roth (enr2116)
Last updated: 3/12/2016

Storytelling with Streaming Data Assignment 3
-------------------

This assignment incorporates use of the categorical distribution on top of previous assignments tracking Wikipedia edit rates. The data stream comes from the Wipedia recent changes API, and notes every time an English-page Wikipedia article has been edited. The rate of the stream is tracked by calculating a moving average over buckets, looking at the 10 most recent articles edited at a time. For this assignment, I decided to investigate the distribution of articles edited by Wikipedia bots, software written by users to automatically make edits. Wikipedia keeps track of certain flags on every edit, including whether or not that edit was made by a bot or not, as well as whether that edit was 'minor' or not (a distinction that has no rigid requirements, but about which more information can be found about at https://en.wikipedia.org/wiki/Wikipedia_talk:Minor_edit). I thought it would be interesting to see how many edits are made by these software bots, and how many of these changes are minor (punctuation, reverts, e.g.) and how many are major content or structural changes.

The following needs to be run to make use of all functionality:

``` python wikipedia_stream_3.py | python wikipedia_diff_3.py | python wikipedia_tweet_3.py &
python insert_minor.py &
python wiki_apy.py```

The webpage displaying the current distribution can be reached at http://localhost:5000/distributions

