import json
from pprint import pprint

relevant_fields = {
    'cast' : ['character', 'name'],
    'directors' : ['department', 'job', 'name'],
    'genres' : ['name'],
    'original_title' : [],
    'overview' : [],
    'production_companies' : ['name'],
    'production_countries' : ['name'],
    'release_date' : [],
    'spoken_languages' : ['name'],
    'tagline' : [],
    'title' : []
}

def strip_field(entry, field, subfields):
    if len(subfields) == 1:
        entry[field] = [e[subfields[0]] for e in entry[field]]
    elif subfields:
        entry[field] = [{k: v for k, v in e.items() if k in subfields} for e in entry[field]]

def cleanup(entry):
    for f, s in relevant_fields.items(): 
        strip_field(entry, f, s)
    # pprint(entry)
    return entry

with open('tmdb.json', 'r') as f:
    db = json.load(f)

clean_data = []
for i in db:
    raw_entry = db[i]
    entry = {}
    for field in relevant_fields:
        entry[field] = raw_entry[field]
    clean_data.append(cleanup(entry))

with open('clean_tmdb.json', 'w') as f:
    json.dump(clean_data, f)
