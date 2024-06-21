
numbers = []

for i in range(1, 11):
    numbers.append(i)


number_of_elements = len(numbers)


print("Numbers:", numbers)
print("Number of elements in the list:", number_of_elements)

start = int(input("Enter the first number: "))
end = int(input("Enter the second number: "))

numbers_between = []


for i in range(start, end + 1):
    numbers_between.append(i)

print("Numbers between", start, "and", end, ":", numbers_between)


start = int(input("Please enter start number: "))
end = int(input("Please enter end number: "))

numbers = []

for i in range(start, end):
    numbers.append(i)

print(min(numbers))
print(max(numbers))
print(sum(numbers))



number =[]
num = int(input("enter how many number you want:"))

for i in range(num):
    num2 = int(input("please enter number:" (i + 1)))
    number.append(num)
print(sum)(number)

#favorite car names
favorite_cars = ["Tesla", "Subaru Legacy", "Audi", "Subaru Impreza", "Porsche 911"]


first_three_cars = favorite_cars[:3]


last_two_cars = favorite_cars[-2:]

print("First three cars:", first_three_cars)
print("Last two cars:", last_two_cars)

third_from_right = favorite_cars[-3]
fourth_from_right = favorite_cars[-4]
result = third_from_right + " and " + fourth_from_right

print("Third and fourth cars from the right:", result)


my_name = "giorgi"


names = [my_name, my_name]

for name in names:
    if name == my_name:
        print("Hello admin")
    else:
        print("Hello user")