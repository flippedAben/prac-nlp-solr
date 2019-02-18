import json
from pprint import pprint

with open('turk_data.json', 'r') as f:
    td = json.load(f)

mapp = {}
for l in td:
    title = l[2]
    d = l[0]
    if title in mapp:
        mapp[title] += [d]
    else:
        mapp[title] = [d]

with open('clean_turk_data.json', 'w') as f:
    json.dump(mapp, f)

tmdb_with_turk = {}
with open('clean_tmdb.json', 'r') as f:
    tmdb_with_turk = json.load(f)

for t in tmdb_with_turk:
    if t['title'] in mapp:
        t['turk_tags'] = mapp[t['title']]
    else:
        t['turk_tags'] = []

with open('clean_tmdb_with_turk.json', 'w') as f:
    json.dump(tmdb_with_turk, f)
