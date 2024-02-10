a={3,5,76,2,34,6,7,211,45,77,12}

# index=0
# for i in a:
#   print("The value at index",index,"is",i)
#   index+=1

# this is the easer way of doing the same as above code
for index,i in enumerate(a):
  print("The value at index",index,"is",i)

print("\n\n")
for index,i in enumerate(a,start=1):
  print("The value at index",index,"is",i)