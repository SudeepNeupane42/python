class person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age
    
    def setter(self,a,b):
        self.name=a
        self.age=b
        
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
p1=person() 
p1.setter("sudeep",20)
print("Name is",p1.getName(),"and Age is",p1.getAge())
    