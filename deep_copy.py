import copy


#shallow copy object and item referancess
#deepcopy copy all and work indivisual 
old = [1,2,3]
#new = copy.copy(old)
new = copy.deepcopy(old)
print(old,new)