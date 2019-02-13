import requests

ENDPOINT = "http://localhost:9000/solr/movies/schema"

r_headers = {"Content-Type": "application/json"}

data = {
  "add-field-type" : {
     "name":"AnalyzedText",
     "class":"solr.TextField",
     "positionIncrementGap":"100",
     "analyzer" : {
        "tokenizer":{
           "class":"solr.StandardTokenizerFactory" },
        "filters":[{
           "class":"solr.LowerCaseFilterFactory"}]}}
}

r = requests.post(ENDPOINT, json=data, headers=r_headers)

print(r.status_code)