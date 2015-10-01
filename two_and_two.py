#!python2
# -*- coding: utf-8 -*-

import sys, random, time

def makeTweets():
	# verbose
	v = False
	v1 = False

	# input file
	argfile = "sentences.txt"

	# read input file
	filename = open(argfile,'r')
	f = filename.readlines()
	filename.close()


	# make a list
	words = ["a word treble", "a word treble"]

	frequency = {"a word treble": 0}

	# build a dictionary of sequential word tuples
	for line in f:
		precedingWord1 = None
		precedingWord2 = None
		for word in line.split(" "):
			if precedingWord1 and precedingWord2:
				if v1: print "Word: " + word
				if v1: print "PrecedingWord1: " + precedingWord1
				if v1: print "PrecedingWord2: " + precedingWord2
				
				words.append(precedingWord2.rstrip() + " " + precedingWord1.rstrip() + " " + word.rstrip())
			precedingWord2 = precedingWord1
			precedingWord1 = word

	# count the frequency of each word tuple, and add them to a dict
	for tuple in words:
		if tuple in frequency:
			frequency[tuple] += 1
		else:
			frequency[tuple] = 1

	counter = 15

	while counter > 0:
		if v: print "-----------------" + str(counter)
		# choose a random treble to start the sentence
		sentence =  random.choice(frequency.keys())

		sentenceEnd = False
		
		flipper = 0

		# keep adding to the sentence while it is less than 138 characters and
		# there are still word tuples to string together
		while (len(sentence) < 138) and (not sentenceEnd):
			if v: print "Sentence: " + sentence
			lastWord = sentence
			
			# separate the two last words in the sentence
			lastWord = lastWord.split(" ")[-2] + " " + lastWord.split(" ")[-1]
			if v: print "Sentence after split: " + sentence
			if v: print "Last word: " + lastWord
			
			sentenceEnd = True
			
			possibilities = []
			del possibilities[:]
			
			
			for key in frequency:
				thetuple = key.split(" ")
				
				if lastWord == (thetuple[0] + " " + thetuple[1]):
					if v1: print lastWord + " <-> " + str(thetuple)
					possibilities.append(thetuple)
			
			if v: print len(possibilities)
			if len(possibilities) != 0:
				if v: print "Sentence: " + sentence
				newrand = random.choice(possibilities)
				if v: print "Newrand: ", newrand
				sentence = sentence + " " + newrand[2]
				sentenceEnd = False
				"""if lastWord == thetuple[0]:
					if v: print "Key: " + thetuple[0]
					sentence = sentence + " " + thetuple[1]
					sentenceEnd = False
					break"""
			if v: time.sleep(0.5)

		if v: print sentence
		while len(sentence) > 138:
			if v: print "Shortening...\n\n\n\n\n\n\n\n\n"
			shortened = sentence
			shortened = shortened.split(" ")
			del shortened[0]
			sentence = " ".join(shortened)
			if v: time.sleep(2)
		
		# add the finishing touch
		sentence = sentence.rstrip()
		
		if (sentence[-1] != ".") and (sentence[-1] != "!") and (sentence[-1] != "?"):
			sentence = sentence + "."
		
		sentence = sentence[:1].upper() + sentence[1:]
		if v: print sentence

		# put the sentence in the ebook
		output = open("ebooks.txt", 'a')

		output.write(sentence + "\n")

		output.close()
		
		counter -= 1

	if v: print "Done!"
	
if __name__ == "__main__":
	makeTweets()
