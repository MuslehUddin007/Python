from functools import reduce

data = [1,2,3,4,5]
multiplier = lambda x,y: x*y
print(reduce(multiplier,data))
