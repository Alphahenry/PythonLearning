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
rest1.open()

                                                                                                                                                                                                                                                                                                                                                                                                