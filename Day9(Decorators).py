def greet(fx):
    def mfx(*args, **kwargs):
        print("Hello!")
        fx(*args,**kwargs)
        print("Thank you.")
    return mfx

@greet
def sum(a,b):
    sum=a+b
    print(f"the sum is {sum}")   

sum(1,2)