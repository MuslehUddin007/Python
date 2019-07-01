#without list comprehention

squares = []
for i in range(1,101):
    squares.append(i**2)
print(squares)

#with list comprehention

squares2 = [i**2 for i in range(1,101)]
print(squares2)

movies = [("Citizen Kane",1941),("Spirited Away",2001),("It's a WOnderful life",1946),
("Gattace",1997),("No Country for Old Men",2007),("Rear window",1954),
("The Lord of the Rings: The Fellowship of the Ring",2001),("Groundhog Day",1993),
("Close Encounters of the Third Kind",1997),("The Royal Tenenbaums",2001),("The Aviator",2004),
("Raiders of the Lost Ark",1981)]

pre2k = [title for (title,year) in movies if year < 2000]
print(pre2k)
