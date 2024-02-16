class employee:
    def __init__(self, name, id):
        self.name = name
        self.id=id
        
    def showDetails(self):
        print(f"The name of employee {self.id} is {self.name}")
        
class developer(employee):
    def greet(self):
        print("HI i'm a developer.")
        
e1=employee("sudeep",21)
e1.showDetails()
d1=developer("shrijana",19)
d1.greet()
d1.showDetails()
