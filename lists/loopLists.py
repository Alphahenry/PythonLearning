cars = ["benz", "mazda", "buggatti", "porche", "alfa romeo"]

for car in cars:
    print(f"This {car.title()} is a wonderful car!")
 
    

for c in cars[:3]:
    print(c)
    


#Having the same cars(copying)

friends_car = cars[:]

print(friends_car)