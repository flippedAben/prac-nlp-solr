import requests

ENDPOINT = "http://localhost:9000/solr/movies/query"

r_headers = {"Content-Type": "application/json"}

query_params = {'df':'title','q':'Space Jam'}

query_response = requests.get(ENDPOINT, params=query_params, headers=r_headers)

print(query_response.status_code)

response_parsed = (''.join(query_response.json()["response"]["docs"][0]["title"])).replace("'", "-").split("-")[0]

print(response_parsed)