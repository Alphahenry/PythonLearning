#a phone model
class Phone:
    def __init__(self,name, model, price,ScreenSize,year):
        self.name = name
        self.model = model
        self.price = price
        self.ScreenSize = ScreenSize
        self.year = year
        
    def avialable(self):
        print("The phone is available now")
        
    
    
    
class Redmi(Phone):
    def __init__(self, name, model, price, ScreenSize, year,color):
        super().__init__(name, model, price, ScreenSize, year)
        self.color = color
        
    def description(self):
       
        info = f"This is a {self.name} phone, {self.price} ksh,{self.color} {self.ScreenSize}, {self.year} year of manufacture"
        return info
    
    
myPhone = Redmi("redmi","x21",34000, "black","16inches",2025)

myPhone.avialable()
print(myPhone.description())