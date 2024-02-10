#you cannot make changes to a tuple directly so firt you have to convert it into a list and then you can make changes to it.
names = ("sudeep", "sirijana", "reegan")
list1=list(names)
list1.append("eliott")
list1.pop(2)
list1[1]="stupid"
names=tuple(list1)
print(names)

#concanating tuples
tuple1=("a","b","c")
tuple2=(1,2,3,4,3,)
tuple3=tuple1+tuple2
print(tuple3)

#counting the number of times a value is present in a tuple
print(tuple3.count(3))

#searching a certain value in tuple between a certain index
print(tuple3.index("a",0,7))