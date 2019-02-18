#! /usr/bin/env python3

import json
import os
import re
from fnmatch import fnmatch
from pprint import pprint

# only take the latest reddit_data file
reddit_data = {}
fns = os.listdir('.')
fns.sort(key=lambda x: os.path.getmtime(x))
latest_fn = ''
for fn in fns:
    if fnmatch(fn, 'reddit_data_*.json'):
        latest_fn = fn
        with open(fn, 'r') as f:
            reddit_data = json.load(f)
        break

# load in tmdb titles
with open('../tmdb.json', 'r') as f:
    db = json.load(f)

reddit_titles = reddit_data.keys()

total = 0
results = {}
for i in db:
    entry = db[i]
    t = re.sub(r'([^\s\w]|_)+', '', entry['title'].lower().strip())
    if t in reddit_titles:
        results[entry['title']] = reddit_data[t]
        total += 1

print(f'Got a total of {total} movies in both data sets.')

with open('clean_' + latest_fn, 'w') as f:
    json.dump(results, f)
