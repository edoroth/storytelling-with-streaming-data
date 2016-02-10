Storytelling with Streaming Data
Assignment 1

Edo Roth (enr2116)
-------------------

 The submission url is at http://www.columbia.edu/~enr2116/wikipedia.html.

 This site shows a live stream of articles that have recently been edited on Wikipedia.

 Each event in the stream represents one article on Wikipedia's English domain that has been changed in any way. These changes could involve editing text, changing a small amount of punctuation, adding or removing a reference, or more. Sometimes, they are changes that simply revert previous edits because of suspicious activity or suspected incorrect information. 

 The stream displayed on the website only consists of changes to main article pages. Wikipedia also has other kinds of pages -- for instance, "Talk" pages are discussion pages where users can discuss content and potential edits, and "Category" pages are pages that include no written information, but just group other Wikipedia articles together. Again, these types of edits (which are made roughly about as frequently as article edits) are not included.

 Each edit includes a list of information about that revision, including various internally usable IDs, timestamp, and editor information. For the purpose of this website, I thought it would be interesting to take a look at the user editors, and their prolificy in editing Wikipedia articles. Because information is only stored about registered users, I removed from the display all articles that have been edited by anonymous users.

 These users includes bots, which are written software that make automatic changes based on suspected vandalism or incorrect edits. These bots can be created and managed by anyone as long as they are approved, so I chose to include their activity to give a sense