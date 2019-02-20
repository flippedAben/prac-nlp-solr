#! /usr/bin/env python3

from html.parser import HTMLParser
import json
import praw
import re

class TLDRMoviesHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.data = []

    def handle_data(self, d):
        if d != '\n':
            self.data.append(d.strip())

    def eat_data(self):
        s = self.data
        self.data = []
        return s

LIM = 1000

reddit = praw.Reddit()
subreddit = reddit.subreddit('tldrmovies')

tops = subreddit.top(limit=LIM)

parser = TLDRMoviesHTMLParser()

# Parse raw data
mapp = {}
for s in tops:
    if s.selftext_html:
        parser.feed(s.selftext_html)
        mapp[s.title] = parser.eat_data()

with open('tldrmovies.json', 'w') as f:
    json.dump(mapp, f)
