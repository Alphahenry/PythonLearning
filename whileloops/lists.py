#empty list
empty = []

#list of numbers
num = [1,2,3,4,56]
#delete element

#del num[3]

print(num)

#list of similar values
num2 = [1,2,3,3,6,8,9,9]


#list of strings

cars = ['mazda', "benz", "porsche"]
#add element at the end
cars.append("hammer")
cars.insert(1,"ferrari")

#sorting a list

cars.sort
print(cars)

#getting the length of a list
print(len(cars))

#sorting in reverse

#print(cars.sort(reverse=True))


print(cars)

#check if element is in lists
print("benz" in cars)


#mixed data types

mixed = [1, 3.14, "hello", ]


#accessing elements by index

print(mixed[0])
print(mixed[1])
print(mixed[2])



print(f"I want a {cars[0]} by december")

#removing the last elemnt

rem_element = num.pop()
print("the popped element is " ,rem_element)
print(num)
