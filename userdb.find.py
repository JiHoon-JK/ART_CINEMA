from pymongo import MongoClient

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.ART_Movie_Platform  # 'ART_Movie_Platform'라는 이름의 db를 만듭니다.

user = list(db.userdb.find({}))
print(user)

for i in range(len(user)):
    user_email = user[i]['email']
    print(user_email)