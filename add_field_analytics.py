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
           "class":"solr.ASCIIFoldingFilterFactory", "preserveOriginal":"true"},{
           "class":"solr.LowerCaseFilterFactory"},{
           "class":"solr.KStemFilterFactory"},{
           "class":"solr.StopFilterFactory", "words":"stopwords.txt"},{
           "class":"solr.SynonymGraphFilterFactory", "synonyms":"synonyms.txt"
           }]}}
}

update_field_json = {
  "replace-field":{
     "name":"title",
     "type":"AnalyzedText",
     "stored":true }
}

update_field_type_response = requests.post(ENDPOINT, json=update_field_type_json, headers=r_headers)

print(update_field_type_response.status_code)

update_field_response = requests.post(ENDPOINT, json=update_field_json, headers=r_headers)

print(update_field_response.status_code)

# Update all fields to be of AnalyzedText type