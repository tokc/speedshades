#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Magic
import tweepy, time, sys, random

import two_and_two
 
# argfile = str(sys.argv[1])

# MAGIC
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = ''#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = ''#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = ''#keep the quotes, replace this with your access token
ACCESS_SECRET = ''#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# Counters to store amount of minutes and number of tweets
total_tweet_time = 0
number_of_tweets = 0

while 1:
	print "Opening files..."
	# Read pending tweets file
	filename = open("./ebooks.txt",'r')
	f = filename.readlines()
	filename.close()
	
	# Read tweets archive
	tweetfile = open("tweets.txt", 'r')
	twits = tweetfile.readlines()
	tweetfile.close()
	
	
	tweeted = False
	i = 0
	
	while not tweeted:
		print "f is this length: -------" + str(len(f))
		
		# If there are fewer than two pending tweets
		if len(f) < 2:
			# Make NLG happen
			print "Generating new tweets. \n\n\n\n"
			two_and_two.makeTweets()
			
			# Read files again
			print "Opening files..."
			filename = open("./ebooks.txt",'r')
			f = filename.readlines()
			filename.close()
			
			tweetfile = open("tweets.txt", 'r')
			twits = tweetfile.readlines()
			tweetfile.close()
		
		print "Checking tweet..."
		
		print i
		# If the next pending tweet doesn't match a previously tweeted tweet
		if f[i] not in twits:
			
			# Write tweet to archive
			print "I haven't tweeted this before."
			tweetfile = open("tweets.txt", 'a')
			tweetfile.write(f[i])
			tweetfile.close()
			
			# Tweet
			print "Tweeting \"" + f[i] + "\""
			api.update_status(status=f[i])
			tweeted = True
			
			# Remove tweet from pending tweets
			print "Deleting from backlog..."
			
			print i
			print f[i]
			
			del f[i]
			
			# Write all the other tweets to pending tweets. I guess that's dumb.
			deletename = open("./ebooks.txt",'w')
			
			for l in f:
				deletename.write(l)
			
			deletename.close()
		
		# If the next pending tweet DOES match a previously tweeted tweet
		else:
			print "Found in archive:"
			print f[i]
			# Remove tweet from pending tweets
			print "Deleting from backlog..."
			
			print i
			print f[i]
			
			del f[i]
			
			# Write all the other tweets to pending tweets. I guess that's dumb.
			deletename = open("./ebooks.txt",'w')
			
			for l in f:
				deletename.write(l)
			
			deletename.close()
			
			i += 1
	
	# Pick a sort of random time to wait
	sleepytime = random.randint(2000, 4000)
	
	# Print stuff
	print str(time.strftime("%H:%M:%S")) + " Sleeping for " + str(sleepytime / 60) + " minutes..."
	
	total_tweet_time += (sleepytime / 60)
	number_of_tweets += 1
	
	print "Average tweet time: " + str(total_tweet_time / number_of_tweets) + " minutes."
	
	# Wait for the sort of random amount of time
	time.sleep(sleepytime)
