dic={
  "name":"sudeep","age":19,"gender":"male"
}
print(dic)
print(dic["name"])

#using get function does not throw error when key is not present
print(dic.get("hobby"))

print(dic.keys())
print(dic.values())

for i in dic.keys():
  print(dic[i])

emp1={101:99,122:58,123:78,124:89}
emp2={125:98,126:87,127:67}
emp1.update(emp2)
print(emp1)
emp2.clear()
emp1.pop(125)
print(emp1)
#to remove last value
emp1.popitem()
print(emp1)