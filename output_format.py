print("Md Musleh Uddin",end=" ")
print("Khan",end=" ")
print("Akil")

print("G","F","G",sep="")
print("09","12","2016",sep="-")

#output formatting
name = "Md Musleh Uddin Khan"
age = 20
salary = 50000.25
#Approach 1
print("Name: %s Age: %d Salary: %g"%(name,age,salary))#%f 5 space after point,%g 1 space after point

#Approach 2
print("Name: {} Age: {} Salary: {}".format(name,age,salary))

#Approach 3
print("Name: {1} Age: {2} Salary: {0}".format(salary,name,age)) #maintain the index of tuple

#Approach 4
print("Number one portal is {0}, {1}, and {other}".format("Geeks","for",other="Geekss"))

#Approach 5
print("Geeks : {0:2d}, Portal : {1:.3f}".format(12,00.546))

#Approach 6
print("Geeks: {a:5d}, Portal: {p:5.2f}".format(a=453,p=12.3356))

#Approach 7 """used in dictionary"""
tab = {"geeks":1234,"for":4502,"geek":564412}
print("Geeks: {0[geeks]:d}; For: {0[for]:d}; Geeks: {0[geek]:d}".format(tab))

#Approach 8 
data = dict(fun = "GeeksForGeeks",adj="Portal")
print("I love {fun} computer {adj}".format(**data))

#string style
print("I love programming".center(40,"#"))
st = "I love programming"
print(st.ljust(40,"*"))
print(st.rjust(40,"$"))

#r ignore hex

String1 = "|{:<10}|{:^10}|{:>10}|".format('Geeks','for','Geeks') 
print("\nLeft, center and right alignment with Formatting: ") 
print(String1)

string = "geeks for geeks geeks geeks geeks"
print(string.replace("geeks","Geeks"))
print(string.replace("geeks","Geeks",3))