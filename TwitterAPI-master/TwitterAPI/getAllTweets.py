Skip to content
 

Search…
All gists
GitHub
 @gilbertjiang
@yanofskyyanofsky/tweet_dumper.py
Last active 7 hours ago
  Star 79
  Fork 34
 
 Code
 Revisions 4
 Stars 79
 Forks 34
Embed URL

<script src="https://gist.github.com/yanofsky/5436496.js"></script>

HTTPS clone URL

https://gist.github.com/5436496.git

You can clone with  HTTPS, SSH, or Subversion. 
 Clone in Desktop
 Download ZIP
A script to download all of a user's tweets into a csv
Raw  tweet_dumper.py
#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv

#Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""


def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print "getting tweets before %s" % (oldest)
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print "...%s tweets downloaded so far" % (len(alltweets))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
	
	#write the csv	
	with open('%s_tweets.csv' % screen_name, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)
	
	pass


if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets("J_tsar")
 @greglinch
greglinch commented on Aug 28, 2013
Thanks for posting this script! Just a heads-up on a minor typo in line 36: "gefore" instead of "before"

https://gist.github.com/yanofsky/5436496#file-tweet_dumper-py-L36
@markwk
markwk commented on Sep 24, 2013
Works great. I'm wondering how I'd do this to get the next 3200 after the initial pull.
@riznad
riznad commented on Oct 17, 2013
I am getting error on windows:

C:>C:\Python26\python.exe C:\Python26\tweet_dumper.py
File "C:\Python26\tweet_dumper.py", line 17
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
^
IndentationError: expected an indented block

C:>C:\Python275\python.exe C:\Python26\tweet_dumper.py
File "C:\Python26\tweet_dumper.py", line 17
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
^
IndentationError: expected an indented block
@yanofsky
Owner
yanofsky commented on Nov 1, 2013
@greglinch thanks, fixed!
@markwk to my understanding there is no way to get these without using a 3rd party or asking the user to download their history
@riznad hard to say what's going on there, is is possible an extra space got inserted on that line? There should only be one tab on that line.
@Kaorw
Kaorw commented on Dec 28, 2013
Thanks for great code!
I've modified a bit to grap timeline and save to excel format("xls") using xlswriter.

https://gist.github.com/Kaorw/7594044

Thanks again
@jdkram
jdkram commented on Dec 28, 2013
Thanks for the code.

I switched up the final line (after importing sys) to feed in usernames from shell:

get_all_tweets(sys.argv[1])
@hub2git
hub2git commented on Apr 2, 2014
Dear all, I downloaded the py file. I'm running Linux Mint. In terminal, I did:
python tweet_dumper.py

but I got this:
Traceback (most recent call last):
File "tweet_dumper.py", line 4, in 
import tweepy #https://github.com/tweepy/tweepy
ImportError: No module named tweepy

What am I doing wrong? What must I do?

By the way, I've created a twitter API for myself. In the tweet_dumper.py file, I've entered my 4 Twitter API credentials. And in the last line of the .py file, I've put in the username whose tweets I want to download.

Should I download the zip file from https://github.com/tweepy/tweepy? I'm so lost, but I want to learn.

UPDATE: 
I did
sudo apt-get install python-pip
then
sudo pip install tweepy
.

Then I ran python tweet_dumper.py again. Now I see a csv file! Thanks!!!
@samarthbhargav
samarthbhargav commented on Jul 2, 2014
Fantastic! Thanks!
@tay1orjones
tay1orjones commented on Jul 16, 2014
This worked great! Thanks for this! Had to get pip and tweepy installed, but it worked out great. Also, note that if the targeted user's twitter account is protected, the account used to authorize the api calls must be following the targeted user.
@LifnaJos
LifnaJos commented on Aug 24, 2014
i tried executing the program. there is no error reported.

But no .csv file created.Please help me out

UPDATE : 1

Later it worked.

UPDATE : 2

But now all of a sudden my program show me error as follows and So I repeated all the steps stated by hub2git. Still its not...........Please do help me to trace out

lifna@lifna-Inspiron-N5050:~$ python
Python 2.7.3 (default, Feb 27 2014, 20:00:17) 
[GCC 4.6.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.

import tweepy
Traceback (most recent call last):
File "", line 1, in 
ImportError: No module named tweepy
exit()
@abhishekmm
abhishekmm commented on Sep 17, 2014
i tried executing it using editrocket[http://editrocket.com/download_win.html]
got following error
File "tweet_dumper.py", line 35
print "getting tweets before %s" % (oldest)
^
SyntaxError: invalid syntax
@hub2git
hub2git commented on Nov 10, 2014
Thanks to this script, I succesfully downloaded a user's most recent 3240 tweets.

Line 15 of the script says
** #Twitter only allows access to a users most recent 3240 tweets with this method**

Does anybody know how to download tweets that are older than the 3240th tweet?
@henry-pearce
henry-pearce commented on Nov 27, 2014
I am getting the below, what am I doing wrong? Thanks

File "tweet_dumper.py", line 27, in get_all_tweets
new_tweets = api.user_timeline(screen_name = screen_name,count=200)
File "C:\Python27\lib\site-packages\tweepy-2.3.0-py2.7.egg\tweepy\binder.py", line 230, in _call
return method.execute()
File "C:\Python27\lib\site-packages\tweepy-2.3.0-py2.7.egg\tweepy\binder.py", line 203, in execute
raise TweepError(error_msg, resp)
TweepError: [{u'message': u'Bad Authentication data', u'code': 215}]
@yosun
yosun commented on Jan 31
This seems to only work for tweets from the past year? (For users with more than 3200 tweets)
@sagarjhaa
sagarjhaa commented on Apr 1
Is that any way we can more than 3200 tweets.....I want all the tweets of a particular user?
@freimanas
freimanas commented on May 27
Sweet!

have modified to get tweets with images and store to csv:
id, tweet text, image url

just in case anyone else needs as well:
https://gist.github.com/freimanas/39f3ad9a5f0249c0dc64
@ashu2188
ashu2188 commented on Aug 12
Works great. But have a question. How do I get only the status and not reply or retweets from a user? Is there any way?
@Purptart
Purptart commented on Aug 14
Hi, I'm using python3.4 and tweepy 3.3.0
I'm getting the following error:

File "dump_tweets.py", line 56, in get_all_tweets
writer.writerows(outtweets)
TypeError: 'str' does not support the buffer interface

This error is also thrown for line 55, but I commented it out in an attempt to debug.

I've tried to just include the text of the tweet which is encoded to utf-8 on line 50, but this still throws the same error.

Does anyone have any hints/suggestions?

EDIT: This appears to only occur on Windows. When running the script from an Ubuntu install it works.
@MihaiTabara
MihaiTabara commented on Aug 22
Thanks for posting the script in the fist place - good way to start tweaking with this library. After playing a bit around with it, it seems like the updated versions of the library solve both the "cope with # of requests/window" and the "don't get busted by the error".

parameter for the api to have it deal with the server
use of Cursor to avoid all the # of requests/window reckon
Just in case somebody needs as well, I did a small implementation following the new features here: https://gist.github.com/MihaiTabara/631ecb98f93046a9a454 
(mention: I store the tweets in a MongoDB databases instead of csv files)
@Din1993
Din1993 commented 22 days ago
I am trying to do this for multiple users by including a for loop. Do you know how to have it also print either their name or their screenname? Thanks!
@Sourabh87
Sourabh87 commented 16 days ago
@ Purptart

Just change the line-
with open('%s_tweets.csv' % screen_name, 'wb', encoding='utf-8') as f:
to
with open('%s_tweets.csv' % screen_name, 'w', encoding='utf-8') as f:

b stands for binary actually. and python 3x versions have modified many things. It works for me fine.
@Sourabh87
Sourabh87 commented 14 days ago
@Din1993

we can get the screen_name user name and other information as well. Show me how you are trying to do it for multiple users. (Code snippet)

Thanks
@gilbertjiang
 Markdown supported
Write Preview

Leave a comment
Attach files by dragging & dropping,  Choose Files selecting them, or pasting from the clipboard.
Comment
Status API Training Shop Blog About Pricing
© 2015 GitHub, Inc. Terms Privacy Security Contact Help