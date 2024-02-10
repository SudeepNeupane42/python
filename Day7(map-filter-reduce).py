# Map
def cube(x):
 return x*x*x

list1=[1,2,3,4,5,6]
newlist= list(map(cube,list1))
# newlist= list(map(lambda x:x**3,list1))
print(newlist)

# filter
def filter_function(x):
    return  x%2==0

filtered_list = list(filter(filter_function, list1))  
print(filtered_list)


# reduce
from functools import reduce
print(reduce(lambda x, y : x+y ,list1)) # ((((1+2)+3)+4)+5)+6