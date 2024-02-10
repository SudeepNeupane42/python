a=int(input("enter a number"))

match a:
 case 1:
   print("a is 1")
 case 2:
   print("case is 2")
      
 case _ if a==10:
    print("this is a special case")
 case _:
  print("case is ",a)
