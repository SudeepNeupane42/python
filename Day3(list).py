marks = [12, 56, 32, 98, 12,  45, 1, 4]
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[-3]) #length-3 i.e 8-3 = marksp[5]

#slicing
print(marks[0:5])
print(marks[0:8:2])

#searching for an element in a list
if 10 in marks:
    print("10 is in the list")
else:
    print("10 is not in the list")

if 7 in marks:
  print("7 is present in list")

#same thing applies for string as well!
s="sudeep"
if "d" in s:
  print("yes")
else:
  print("no")

#list comprehension
list2= [i for i in range(4)]
print(list2)
list3=[i*i for i in range(4)]
print(list3) 
list3=[i*i for i in range(10) if i%2==0]
print(list3) 
