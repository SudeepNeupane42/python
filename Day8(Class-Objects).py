class person:
    name="sudeep"
    age=19
    salary=1000000
    address="ilam"
    def info(self):
        print(f"{self.name} lives in {self.address}")
    
a=person()
b=person()
a.name="john"
a.address="usa"
b.name="jina"
b.address="japan"
print(a.name)
a.info()
b.info()
