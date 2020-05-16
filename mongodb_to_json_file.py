from pymongo import MongoClient
client = MongoClient('localhost', 27017)

mongoexport --db ART_Movie_Platform -c Long_movie_list --out longmoviedb_2.json
#mongoexport --db dbsparta -c articles --out articles.json

