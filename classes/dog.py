#modelling the dog
class Dog:
    def __init__(self, name, age):
     self.name = name
     self.age = age
     
     
    def sit(self):
        print(f"{self.name} sit still!")
        
    def bark(self):
        print(f"Roll over")
        
        
dog = Dog("vince", 3)

dog.bark()
dog.sit()