import requests

ENDPOINT = "http://localhost:9000/solr/movies/schema"

r_headers = {"Content-Type": "application/json"}

add_field_type_json = {
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

update_field_type_json = {
  "replace-field-type" : {
     "name":"AnalyzedText",
     "class":"solr.TextField",
     "positionIncrementGap":"100",
     "analyzer" : {
        "tokenizer":{
           "class":"solr.StandardTokenizerFactory" },
        "filters":[{
           "class":"solr.LowerCaseFilterFactory"},{
           "class":"solr.KStemFilterFactory"},{
           "class":"solr.SynonymGraphFilterFactory", "synonyms":"synonyms.txt"
           }]}}
}

update_field_type_response = requests.post(ENDPOINT, json=update_field_type_json, headers=r_headers)

print(update_field_type_response.status_code)