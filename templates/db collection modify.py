from pymongo import MongoClient

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.ART_Movie_Platform  # 'ART_Movie_Platform'라는 이름의 db를 만듭니다.
# Long_movie_list, ART_movie_List

db.ART_movie_list.update_many({}, {'$set': {'liked_cnt': 0, 'commented_cnt': 0, 'searched_cnt': 0}})
db.Long_movie_list.update_many({}, {'$set': {'liked_cnt': 0, 'commented_cnt': 0, 'searched_cnt': 0}})