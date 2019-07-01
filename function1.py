def fnc(x,y,z=0):
    x = x * x
    y = y * y
    z = z * z
    return x,y,z

#ans1,ans2,ans3=fnc(10,20,30)
#print(ans1,ans2,ans3)
#print(fnc(10,20,30))
ans = fnc(10,20)
print(ans[0],ans[1],ans[2])
