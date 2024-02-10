
n=input("enter an odd number: ")
if n=="quit":
    print("no error")
elif int(n)%2==0:
    raise ValueError("the entered number should be odd")
