lst = ["Cat","Bat","Sat","Cat","Mat","Cat","Sat"]

print([[l,lst.count(l)] for l in set(lst)])

print(dict((l,lst.count(l)) for l in set(lst)))