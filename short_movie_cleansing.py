from pymongo import MongoClient

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.ART_Movie_Platform  # 'ART_Movie_Platform'라는 이름의 db를 만듭니다.

db.ART_movie_list.update_many({'genre_1': '공포(호러)'}, {'$set': {'genre_1': '공포'}})

db.ART_movie_list.update_many({'genre_2': '공포(호러)'}, {'$set': {'genre_2': '공포'}})

db.ART_movie_list.update_many({'genre_1': '어드벤처'}, {'$set': {'genre_1': '모험'}})

db.ART_movie_list.update_many({'genre_2': '어드벤처'}, {'$set': {'genre_2': '모험'}})

db.ART_movie_list.update_many({'genre_1': '어드벤처'}, {'$set': {'genre_1': '모험'}})

db.ART_movie_list.update_many({'genre_2': '어드벤처'}, {'$set': {'genre'
                                                             '_2': '모험'}})


db.Long_movie_list.update_many({'main_genre': '느와르'}, {'$set': {'main_genre': '범죄/느와르'}})

db.Long_movie_list.update_many({'second_genre': '느와르'}, {'$set': {'second_genre': '범죄/느와르'}})

db.Long_movie_list.update_many({'main_genre': '범죄'}, {'$set': {'main_genre': '범죄/느와르'}})

db.Long_movie_list.update_many({'second_genre': '범죄'}, {'$set': {'second_genre': '범죄/느와르'}})


db.ART_movie_list.update_many({'genre_1': '범죄'}, {'$set': {'genre_1': '범죄/느와르'}})

db.ART_movie_list.update_many({'genre_2': '범죄'}, {'$set': {'genre_2': '범죄/느와르'}})

db.Long_movie_list.update_many({}, {"$rename":{"main_genre": "genre_1"}})
db.Long_movie_list.update_many({}, {"$rename":{"second_genre": "genre_2"}})