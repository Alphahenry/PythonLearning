#modelling a class car

class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 3000
        
        
    def description(self):
        info = f"This is an {self.make}, {self.model} year of manufacture {self.year}"
        return info
    
    def miles(self):
        mileage = f"The mileage is {self.odometer} km"
        return mileage
    
    def change_odometer(self, mileage):
        self.odometer =  mileage
        print(f"new miles is {mileage}")
        
myCar = Car("audi", "q4", 2019)

print(myCar.description())
print(myCar.miles())
myCar.change_odometer(3530)

        