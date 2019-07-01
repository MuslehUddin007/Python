#g = lambda x: 3*x + 1
#print(g(2))

#full_name = lambda fn,ln: fn.strip().title() + " " + ln.strip().title()
#print(full_name(" Musleh","Uddin "))

name = ["Md Musleh Uddin","Md Mujahid Uddin","Md Musahid Uddin","Umma Aymun Akhi","Ashik","Ridoy","Tanjir Hossine","Moonera","Jemi"]
name.sort(key=lambda n: n.split(" ")[0].lower())
print(name)

def build_quadratic_function(a,b,c):
    """Return the function f(x) = ax^2 + bx + c"""
    return lambda x: a*x**2 + b*x + c

print(build_quadratic_function(3,0,1)(2))