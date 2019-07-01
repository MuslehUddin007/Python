example = set()
example.add(84)
example.add(True)
example.add(3.14157)
example.add("Musleh")
print(example)
"""set do not contain duplicate element""" 
print(len(example))
example.remove(84)
example.discard(50)
print(example)
"""discard is better then remove cause if there is no element
remove will show error but dircard not"""
#clear method is to remove all element of set
#keyword: union, intersection
