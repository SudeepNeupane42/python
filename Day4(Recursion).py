def fact(n):
  if (n==0 or n==1):
    return 1
  else:
    return n*fact(n-1)

f=fact(5)
print(f)
def fib(n):
  if n<=1:
    return n
  else:  
    return fib(n-1)+fib(n-2)

for i in range(5):
  print(fib(i))