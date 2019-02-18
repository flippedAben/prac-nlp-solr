#! /usr/bin/env python3

import datetime as dt
import json
import praw
import re

LIM = 1000

def find_title(s, c, ps):
    for popc in c._replies:
        if 'solved' in popc.body.lower():
            ps.append((c.body.lower(), s.title))
            return True
    return False

def is_norm_title(title):
    return title.isalpha() 

reddit = praw.Reddit()
subreddit = reddit.subreddit('ExplainAFilmPlotBadly')

# Get ~1000 hottest posts
hots = subreddit.hot(limit=LIM)

# Parse raw data
pairs = []
i = 1
for s in hots:
    print('Status: ', i, f'/ {LIM}', end='\r')
    i += 1
    if s.link_flair_text == 'Solved!':
        for c in s.comments:
            if c.body != '[deleted]' and 'solved' not in c.body.lower(): 
                if find_title(s, c, pairs):
                    break

# Clean up raw data and put into dict
# Each title maps to a list of overviews
results = {}
for t, ov in pairs:
    # normalize titles
    t = re.sub(r'([^\s\w]|_)+', '', t.lower().strip())
    if t not in results:
        results[t] = [ov]
    else:
        results[t].append(ov)

# Write to json file
now = dt.datetime.now()
now_date = f'{now.day}-{now.month}-{now.year}'

with open(f'reddit_data_{now_date}.json', 'w') as f:
    json.dump(results, f)
