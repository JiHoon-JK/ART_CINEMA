inFile = None
inString=""
a=""
inFile= open("Long_movie_list.txt", "r", encoding="utf-8")
inList= inFile.readlines()
for inString in inList:
    a +=inString
inFile.close()


# print(a)


z= a.split('}')
# print(z[0]+'}')
# print(z[1]+'}')

all = "},".join(z)
print(all)