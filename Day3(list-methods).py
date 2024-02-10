li=[6,7,3,9,11,5,3]
print(type(li))
print("values of list: ")
print(li)

# to add at the end of list
li.append(1)
print("after adding 1 at the end of list:")
print(li)

#reverse the values of list
li.reverse()
print("after reversing the list:")
print(li)

#sort in accending order
li.sort()
print("after sorting the list:")
print(li)

#sort in descending order
li.sort(reverse= True)
print("after sorting the list in descending order:")
print(li)

#indes of value in list
print("index of value 5 is:",li.index(5))

#count the number of occurence of value in list
print("the occurance of 3 is:",li.count(3),"times")

#value copy is done by refrence in python
m=li
m[0]=100
print("the changed value is",li) 
#change is reflected in original list

#copy of list is done by value in python
ml=li.copy()
ml[0]=200
print("the changed value using copy function is:\n",li)
#change is not reflected in original list but change happend in new list
print("the value of ml,ie. copy of list is:\n",ml)

#to insert at a particular index 
li.insert(5,68) #insert 68 at index 5
print("the list after inserting is:\n", li)

#extend
a=[1,2,3,4]
b=[5,6]
a.extend(b)
print("the extended list is:",a)

#concatenate 
c=[7,8,9]
d=a+c
print("the concatinated list is:",d)
