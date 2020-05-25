input("이름, 생년, 생일(네 자리수)을 입력하세요")
name = input("이름: ")
b_year = int(input("생년: "))
b_date = int(input("생일: "))
b_month = b_date // 100
b_day = b_date % 100

c_year=2018
c_month=8
c_day=11

if c_month > b_month or c_month == b_month and c_day >=  b_day:
  age=c_year-b_year
elif c_month == b_month and c_day < b_day or c_month < b_month :
 age=c_year-b_year-1

print("{}님의 만 나이는 {}세입니다.".format(name,age))