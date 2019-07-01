import math
import statistics
radii = [2,5,7.1,0.3,10]

def area(r):
    """Area of a circle with radius 'r'."""
    return math.pi * (r**2)

list(map(area,radii))

temps = [("Berlin",29),("Cairo",36),("Buenos Aires",29)]

c_to_f = lambda data:(data[0],(9/5)*data[1]+32)
list(map(c_to_f,temps))

data = [1.3,2.7,0.8,4.1,4.3,-0.1]
avg = statistics.mean(data)
print(avg)
print(list(filter(lambda x: x>avg,data)))


