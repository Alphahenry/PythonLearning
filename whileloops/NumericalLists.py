#using range function
for num in range(0, 6):
    print(num)
    


#use range to make a list of numbers

int_num = list(range(10,21))
print(int_num)


#create an empty list and append values to it

squares = []

for num in range(1,10):
    square = num ** 2
    squares.append(square)
    
print(squares)
