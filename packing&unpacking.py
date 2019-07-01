def fun(**d):
    print(type(d))
    for key in d:
        print("%s = %s"%(key,d[key]))

fun(Name="Md Musleh Uddin",ID="181-35-2313",Language="Python")