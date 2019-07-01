def divide(a,b):
    try:
        return a/b
    except Exception:
            print("You can't divide by zero ",Exception)
    finally:
            print("inside finally")

a = 1.0
b = 2
print(divide(a,b))
print(divide(5,0))