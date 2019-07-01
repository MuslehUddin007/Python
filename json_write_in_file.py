import json
movie = {}
movie["title"] = "Minority Report"
movie["director"] = "Steven Spielberg"
movie["composer"] = "John Williams"
movie["actors"] = ["Tom Cruise","Colin Farrell","Samantha Morton","Max von Sydow"]
movie["is_awesome"] = "True"
movie["budget"] = 102000000
movie["cinematographer"] = "Janusz Kami\u0144ski"

file = open("D:\\python\\movie_2.txt","w",encoding = "utf-8")
json.dump(movie,file,ensure_ascii=False)
file.close()