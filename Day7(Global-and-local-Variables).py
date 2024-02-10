x=7
print(f"the values of x is {x}")

def fun1():
    x=6
    print(f"inside the function, the value of x is {x}")

def fun2():
 global x
 x=10
 print(f"now the value of x changed to {x}")


fun1()
print(f"after calling fun1() the value of x is still {x}")
fun2()
print(f"after calling fun2() the vlaue of x is {x}")