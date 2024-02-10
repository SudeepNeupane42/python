a=100
b="1"
c=100.5
#explicit type cast
print(a+int(b))
#implicit type cast
d=a+c
print(d)

#performing basic arithmetic operations by taking user input 
a=input("enter the first number :")
b=input("enter the second number :") 
a=int(a)
b=int(b)
print("the sum of the two numbers is :",a+b)
print("the difference of the two numbers is :",a-b)
print("the product of the two numbers is :",a*b)
print("the quotient of the two numbers is :",a/b)
print("the remainder of the two numbers is :",a%b)
print("the exponential of the two numbers is :",a**b)
print("the floor division of the two numbers is :",a//b)

# printing string on multiple lines
a="""hello
hi 
how 
are 
you"""
print(a)

#print " " in between the string
i='he said"he is sick"'
print(i)