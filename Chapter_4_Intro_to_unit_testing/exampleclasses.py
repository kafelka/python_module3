class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        print(self.name, self.age, self.gender)
        
        def getDetails(self):
            print(self.name, self.age, self.gender)
        
    def changeName(self, newName):
        self.name = newName
        
    def tenperless(self, salary):
        newSalary = salary - (salary*0.1)
        
        
        
if __name__ == "__main__":
    aminat = Person("Aminat", 20, "Female")    
    aminat.getDetails()
    aminat.changeName("Aminat2")
    aminat.getDetails()