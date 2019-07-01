import json
json_file = open("D://python//movie_1.txt","r",encoding = "utf-8")
movie = json.load(json_file)
json_file.close()

#print(movie)
#print(movie["title"])
#print(movie["actors"])

json.dumps(movie,ensure_ascii=False)

