import requests
import decimal

ENDPOINT = "http://localhost:9000/solr/movies/query"

r_headers = {"Content-Type": "application/json"}

correct_movie = "Space Jam"

query_params = {'df':'title','q':'Space Jam'}

query_response = requests.get(ENDPOINT, params=query_params, headers=r_headers)

print(query_response.status_code)

response_parsed = (''.join(query_response.json()["response"]["docs"][0]["title"])).replace("'", "-").split("-")[0]

print(response_parsed)

correct_response_counter = 0

for i in query_response.json()["response"]["docs"]:
	movie_title = (''.join(i["title"])).replace("'", "-").split("-")[0]
	if movie_title == correct_movie:
		correct_response_counter += 1

total_movies = query_response.json()["response"]["numFound"]

precision = decimal.Decimal(correct_response_counter)/decimal.Decimal(total_movies)

print(precision)