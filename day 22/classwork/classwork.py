def calculate_average(numbers):

    total_sum = sum(numbers)

    count = len(numbers)

    average = total_sum / count

    return average


numbers = [1, 2, 3, 4, 5]

average = calculate_average(numbers)

print("The average is:", average)

def greet(name="guest"):
    print("Hello, " + name + "!")


greet("giorgi")  
greet()         

