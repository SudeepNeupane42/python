s1={1,2,3,4,5}
s2={3,4,5,6,7}

#union & update
print("union & update")
print(s1.union(s2))
print(s1)
s1.update(s2)
print(s1)

s1={1,2,3,4,5}
s2={3,4,5,6,7}
#intersection & intersection_update
print("\nintersection & intersection_update")
print(s1.intersection(s2))
print(s1)
s1.intersection_update(s2)
print(s1)

s1={1,2,3,4,5}
s2={3,4,5,6,7}
#symmetric difference =AUB-A∩B
print("\nSymmetric difference")
print(s1.symmetric_difference(s2))

#difference & difference_update
print("\ndifference & difference_update")
print(s1.difference(s2))
print(s2.difference(s1))
s1.difference_update(s2)
print(s1)

s1={1,2,3,4,5}
s2={3,4,5,6,7}
s3={8,9,10,11}
#isdisjoint
print("\nisdisjoint")
print(s1.isdisjoint(s2))
print(s3.isdisjoint(s2))

s1={1,2,3,4,5}
s2={3,4,5,6,7}
s3={1,2}
#issuperset & subset
print("\nissuperset")
print(s1.issuperset(s2))
print(s1.issuperset(s3))
print(s3.issubset(s1))

s1={1,2,3,4,5}
#remove
print("\nremove")
s1.remove(3)
print(s1)
#discard is similar to remove but if the element is not present in the set it does not raise an error
s1.discard(7)

#pop - pops a random value from set
s1= {7,6,"sudeep","john",3,4,5}
print("\npop")
item=s1.pop()
print(item)

#delete a set
del s1

#check if item exists
s1= {7,6,"sudeep","john",3,4,5}
if "sudeep" in s1:
  print("sudeep is present")
else:
  print("sudeep is not present")