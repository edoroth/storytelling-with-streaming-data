Edo Roth (enr2116)  
Last updated: 2/10/16  

Storytelling with Streaming Data Assignment 1
-------------------

 The submission url is at http://www.columbia.edu/~enr2116/wikipedia.html. To start the websocket which is necessary for information to appear on the website, the following command needs to be run inside of this directory:

 ` websocketd --port=8080 python wikipedia_stream.py `

 This site shows a live stream of articles that have recently been edited on Wikipedia.

 Each event in the stream represents one article on Wikipedia's English domain that has been changed in any way. These changes could involve editing text, changing a small amount of punctuation, adding or removing a reference, or more. Sometimes, they are changes that simply revert previous edits because of suspicious activity or suspected incorrect information. 

 The stream displayed on the website only consists of changes to main article pages. Wikipedia also has other kinds of pages -- for instance, "Talk" pages are discussion pages where users can discuss content and potential edits, and "Category" pages are pages that include no written information, but just group other Wikipedia articles together. Again, these types of edits (which are made roughly about as frequently as article edits) are not included.

 Each edit includes a list of information about that revision, including various internally usable IDs, timestamp, and editor information. For the purpose of this website, I thought it would be interesting to take a look at the user editors, and their experience in editing Wikipedia articles. Because information is only stored about registered users, I removed from the stream all articles that have been edited by anonymous users. Thus, the only events displayed on the webpage are edits made by users who have officially registered an account (from rough observations, this is a huge majority of all total edits).

 It's interesting to note that these users includes bots, which are written software that make automatic changes based on suspected vandalism or incorrect edits. These bots can be created and managed by anyone as long as they are approved, so I chose to include their activity to give a sense of total Wikipedia editing activity. All bot users are designated with the word 'bot' somewhere in the username.

 In the file 'wikipedia_stream.py', the stream is consumed from Wikipedia's API, which returns chunks of recent changes. The stream is filtered slightly, and another call to the API is made to retrieve total user edit information. Then, the changes are formatted with article name, username, and total edits made by that user and printed to stdout. When a websocket is created from this python program, the wikipedia.html page connects to the websocket and displays the printed information. Again, the site is live at http://www.columbia.edu/~enr2116/wikipedia.html, but can also be viewed locally.