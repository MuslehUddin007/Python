import random
import string

def rand_pass(size):
    generate_pass = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(size)])
    return generate_pass

password = rand_pass(10)
print(password)

def rand_pass2(size,scope = string.ascii_letters + string.digits): #If want lower letter only use string.ascii_lowercase
    generate_pass = "".join([random.choice(scope) for n in range(size)]) #If want upper letter only use string.ascii_uppercase
    return generate_pass

password1 = rand_pass2(10,"mdmuslehuddinkhan")
print(password1)