
# def square(x):
#     return x*x

'''Instead of doing that you can do it faster using lambda but its the same thing'''
square=lambda x:x*x
cude=lambda x:x*x*x
power4=lambda x:x**4
# avg=lambda x,y: (x+y)/2
avg=lambda x,y,z: (x+y+z)/2

def mul(a,b):
    return a*b

print(square(5))
print(cude(5))
print(power4(5))
print(avg(10, 20, 50))
