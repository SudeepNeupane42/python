class person:
    def __init__(self,a,b):
        self.name=a
        self.location=b
        print(f"{self.name} is from {self.location}")

class defaultc:    
    def __init__(self):
        print("This is a default constructor")
        
a=person("sudeeep","ilam")
b=defaultc()
