import json
from collections import OrderedDict
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.ART_Movie_Platform

file_data = OrderedDict()

datas = list(db.ART_movie_list.find({}))
print(datas)

for data in datas:
    file_data["_id"] = data["_id"]
    file_data["title"] = data["title"]
    file_data["poster"] = data["poster"]
    file_data["director"] = data["director"]
    file_data["summary"] = data["summary"]
    file_data["genre_1"] = data["genre_1"]
    file_data["genre_2"] = data["genre_2"]
    file_data["commented_cnt"] = data["commented_cnt"]
    file_data["liked_cnt"] = data["liked_cnt"]
    file_data["searched_cnt"] = data["searched_cnt"]

print(json.dumps(file_data, ensure_ascii=False, indent="\t"))
