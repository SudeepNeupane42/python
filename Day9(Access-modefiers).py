class employee:
    def __init__(self, name):
        self.__name=name
                
e=employee("sudeep")
# print(e.name) cannot be accessed
print(e._employee__name) #can be accessed