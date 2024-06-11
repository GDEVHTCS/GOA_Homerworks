name = 0  
while name < 10:
    print("Giorgi")
    name += 1

#0- დან 10 ის ჩათვლით შეკრება ლუწი რიცხვების
total = 0
i = 0
while i <= 10:
    if i % 2 == 0:
        total += i
    i += 1
print("The total is:", total)

#guess game
num = 0

while num != 5:
    num = int(input("enter correct number :"))

    if num == 5:
     print('you won!!')

    else:
     print("you lose try again")