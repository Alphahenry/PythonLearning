#modellng a restaurant
class Restaurant:
    def __init__(self,name, cusine):
        self.name = name
        self.cusine = cusine
        
        
    def describe(self):
        info = f"The name of the restaurant is {self.name} and offers {self.cusine} cuisine"
        return info
        
    def open(self):
        print('The restuarant is open')  
        
        
rest1 = Restaurant("Al-Fatiha", "Arabic")
print(rest1.describe())

#our street branch for kids offering Ice cream
#our street branch for kids offering Ice cream

class Icecreamstand(Restaurant):
    def __init__(self, name, cusine):
        super().__init__(name, cusine)
        
        self.flavours = ["strawberry", "caramel", "chocolate", "vanilla"]
        
    def offer_flavors(self):
        print("offers available include: ")
        for flav in self.flavours:
            print(flav)
stand1 = Icecreamstand("opium","ice")
print(stand1.describe())
stand1.open()
stand1.offer_flavors()
                                                                                                                                                                                                                                                                                                                                                                                                