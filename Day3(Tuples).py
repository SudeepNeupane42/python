#tuple cannot be changed
tup=(1,2,3,4,5,"nums")
print(type(tup))
print(tup)
print(tup[0])
print(tup[1])

#slicing is done by storing in new tuple
tup2=tup[1:4]
print(tup2)  