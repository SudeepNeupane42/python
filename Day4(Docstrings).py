#Docstrings are the string literals that appear right after the definition of a function, method, class, or module.
#note that docstrings must be written right below the function name

def sum(a,b):
  '''Takes in a number a,b and returns the sum of a and b'''
  return a+b

s=sum(5,10)
print(s)
#printing the docstring of sum function
print(sum.__doc__)
