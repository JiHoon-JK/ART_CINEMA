from pymongo import MongoClient

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.ART_Movie_Platform  # 'ART_Movie_Platform'라는 이름의 db를 만듭니다.

db.ART_movie_list.remove({})
db.Long_movie_list.remove({})
