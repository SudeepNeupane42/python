def sum(a,b):
  sum=a+b
  return sum
abc=10
def average(a=5,b=6):
  print("The average is",(a+b)/2)
        
def sub(a,b):
  pass  #baad meh lekhunga

def average2(*num): #any num of arguements
  sum=0
  for i in num:
    sum=sum+i
  print("Average is: ",sum/len(num))

def name(**name):
  print(name)
c=7
m=10
i=sum(c,m)
print("sum is:",i)
#types of parameters
average()
average(5)
average(b=9)
average(5,9)
average(b=8,a=7)
average2(1,2)
average2(1,2,3)
average2(1,2,4)


# dict={"name":"sudeep", "age": "19"}
# print(dict)
name(name="sudeep", age="19")