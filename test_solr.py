import requests
import json
import decimal

ENDPOINT = "http://localhost:9000/solr/movies/query"

r_headers = {"Content-Type": "application/json"}

with open('./goldStandardWithSeries.json') as raw_turk_data:
	turk_data = json.load(raw_turk_data)

precision_total_score = 0
recall_total_score = 0
total_rank = 0
total_row_count = 0
total_correct_response_count = 0;



for movie_row in turk_data:
	movie_description = movie_row[0]
	correct_movie = movie_row[2]
	query_params = {'defType':'edismax', 'qf':'cast.name cast.character directors.name genres original_title overview production_companies production_countries release_date spoken_languages tagline',
	                'q':movie_description}
	query_response = requests.get(ENDPOINT, params=query_params, headers=r_headers)
	#print(query_response.status_code)
	correct_response_counter = 0
	rank = 0
	for i in query_response.json()["response"]["docs"]:
		rank += 1
		movie_title = (''.join(i["title"])).replace("'", "-").split("-")[0]
		if movie_title == correct_movie:
			correct_response_counter += 1
			total_rank += rank

	total_movies = query_response.json()["response"]["numFound"]

	if total_movies > 0:
		precision = decimal.Decimal(correct_response_counter)/decimal.Decimal(total_movies)
		recall = 1
	else:
		recall = 0

	precision_total_score += precision
	recall_total_score += recall
	total_row_count += 1

	total_correct_response_count += correct_response_counter

	print(total_row_count)


precision_total_avg = decimal.Decimal(precision_total_score) / decimal.Decimal(total_row_count)
recall_total_avg = decimal.Decimal(recall_total_score) / decimal.Decimal(total_row_count)
rank_total_avg = decimal.Decimal(total_rank) / decimal.Decimal(total_correct_response_count)

print "Average Precision:", str(precision_total_avg)
print "Average Recall:", str(recall_total_avg)
print "Average Rank:", str(rank_total_avg)