import json
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
import csv

stopwords = set(stopwords.words('english'))

with open('clean_tmdb.json') as f:
    data = json.load(f)

def getListOfSyn(word):
    res = set()
    #res.add(word)
    syns = wordnet.synsets(word)
    for s in syns:
        syn = s.lemmas()[0].name()
        if syn != word:
            if '_' not in syn:
                res.add(syn)
    return res

synMap = dict()

for d in data:
    title = d['title']
    if title:
        for w in title.split():
            word = w.lower()
            if word not in stopwords:
                if word not in synMap:
                    syns = getListOfSyn(word)
                    if syns != set():
                        synMap[word] = syns
    overview = d['overview']
    if overview:
        for w in overview.split():
            word = w.lower()
            if word not in stopwords:
                if word not in synMap:
                    syns = getListOfSyn(word)
                    if syns != set():
                        synMap[word] = syns

f = open("syn.txt", "w")
for w in synMap:
    f.write(w + ", ")
    f.write(", ".join([str(x) for x in synMap[w]]))
    f.write("\n")
    #f.write(synMap[w], sep = ", ")
