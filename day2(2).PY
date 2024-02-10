a="apple"
 #printing each characters of apple seperately
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

#string slicing
b="apple boy"
print(b[6:9])
print(b[:4])
print(a[0:])
print(a[:])
print(a[0:-1]) #total index -1 ie 4-1=3
#print(a[-1:-3]) 4-1=3 and 4-3=1 so it wil not work
print(a[-5:5]) #

#string length
c=len(a)
print("the length of",a,"is",c)
print("the length of",b,"is",len(b))

