def find():
  li=[1,2,3,4]
  try:
    i=int(input("enter an index:"))
    print(li[i])
    return 1
  except:
    print("error occured")
    return 0

  finally:
    print("this is always executed")
    

a=find()
print("the value of a is:",a)