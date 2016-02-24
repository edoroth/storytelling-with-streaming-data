Edo Roth (enr2116)

Exercise 2 submission
---------------------

This project utilizes the same Wikipedia API I used in Exercise 1. It receives information on the most recent Wikipedia article changes. Information on the details of the stream can be found in the README for Exercise 1. For this exercise, I chose to specifically monitor article changes about the remaining major 2016 U.S. Presidential candidates. I monitor all recent changes to Wikipedia articles whose titles contain the full name of any of these 7 candidates (in no particular order: Donald Trump, Hillary Clinton, Bernie Sanders, John Kasich, Marco Rubio, Ted Cruz, Ben Carson). The rate of the stream is calculated, and is averaged out over the last 3 edits made. If more than 3 edits are made in a period of 2 minutes, this is regarded as an uptake in the rate of the stream (a particularly active period of editing for these articles). In this case, an alert (along with the names of the recent articles edited) is sent to a twitter bot on my personal account, @dropshot_lob. Every article name that appears in a tweet corresponds to distinct article edits, so tweets that contain identical article names (see sample tweet below) correspond to separate edits made at different timestamps as reported by Wikipedia.

I thought this was an interesting alert to measure because this is a hot topic these days, and I wanted to measure editing activity on articles that many people view as important (and also potentially contentious or controversial). While this exceeds the scope of this exercise, it would be interesting to compare editing rate with recent events or changes in public opinion concerning certain candidates, to see if this encourages more rampant editing of their corresponding Wikipedia articles. I found the threshold I chose to be a decent indicator of a particularly active period of editing, as editing rate does appear to break this threshold a few times a day, although it is not an extremely common occurence.

The code consists of three python files: `wikipedia_stream_2.py` , `wikipedia_diff.py`, and `wikipedia_tweet.py`.

The code can be run with the following command: `python wikipedia_stream_2.py | python wikipedia_diff.py | python wikipedia_tweet.py`
(or by running the provided bash script alert_bot.sh)

Sample tweet: 


![alt tag](https://i.gyazo.com/a298ebb670adca81705d429ecae0ab65.png)
