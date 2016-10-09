#!/usr/bin/env python3

import sys
import os
import feedparser
from subprocess import call
from bs4 import BeautifulSoup

def printLine():
    terminalRows, terminalColumns = os.popen('stty size', 'r').read().split()
    for i in range(0, int(terminalColumns)):
        sys.stdout.write("-")
    print("\n")


def feedContents(feed):
	for post in feed.entries:
    		printLine()
   	 	soup = BeautifulSoup(post.description, "lxml")
    		texts = soup.findAll(text = True)
    		print ''.join(texts)
		print ''
		print post.link
	printLine()



feedBlog = feedparser.parse('https://communityblog.fedoraproject.org/feed/')
#feedPlanet = feedparser.parse('http://fedoraplanet.org/atom.xml')

feedContents(feedBlog)
#feedContents(feedPlanet)
