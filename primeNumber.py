import time
import math
def is_prime_v1(n):
    """Return 'True' if 'n' is a prime number. False otherwise"""
    if n==1:
        return False
    
    for d in range(2,n):
        if n%d ==0:
            return False
    return True

def is_prime_v2(n):
    if n==1:
        return False
    
    max_divisor = math.floor(math.sqrt(n))
    for d in range(2, 1+ max_divisor):
        if n%d == 0:
            return False
    return True

def is_prime_v3(n):
    if n==1:
        return False
    
    if n==2:
        return True
    if n>2 and n%2 == 0:
        return False
    
    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1+max_divisor,2):
        if n%d == 0:
            return False
    return True

for n in range(1,21):
    print(n,is_prime_v1(n))
