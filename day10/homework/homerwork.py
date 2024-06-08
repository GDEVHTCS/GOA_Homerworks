#დავალება 1
for i in range(21): #20 ის ჩათვლით რიცხვების გამოტანა
    print(i)

#დავალება 2
num = int(input("Enter a number: ")) #მომხმარებლის შემოტანილი რიცხვი

if num % 2 == 0:
    print("Number is even") #დაიბეჭდება მხოლოდ ლუწი რიცხვის შემთხვევაში

#დავალება 3
for i in range(21):
    if i % 2 ==0:
        print(i)

#დავალება 4
sum = 0
for i in range(51, 101): #50 დან 100 ის ჩათვლით რიცხვები
    sum += i  #თითოეული რიცხვის მიმატება
print(sum) #დაბეჭდვა

#დავალება 5
for i in range(1, 51):  #1 დან 50 ის ჩათვლით რიცხვები
    if i % 5 == 0: #5 ის ჯერადი რიცხვები
        print(i) #დაბეჭდვა

#დავალება 6
num1 = int(input("enter number :")) #შემოიტანეთ რიცხვი
for i in range(1): #გამეორება for ციკლით ერთხელ
    if 1000 < num1: #თუ ათასი ნაკლებია შემოტანილ რიცხვზე მაშინ უდიდესია
        print('უდიდესი') #დაიბეჭდოს უდიდესი

num2 = int(input("enter number :"))#რიცხვის შემოტანა
for i in range(1): #გამეორება ერთხელ
    if 1000 > num2: # თუ მეტია შემოტანილ რიცხვზე ათასი მაშინ უმცირესია
        print('უმცირესი')

#დავალება 7
#ცვლადები - #num1 = 5 #print(num1)
#ინფუთები: integer, string და float - #int(input("enter numb:))  #str(input("enter name:))         #float(input("enter numb:))
#boolean - print(true and false)#true: print(false or false)#false
#გამეორებები- for i in range():
#if-elif-else: if i >= 30: 

#დავალება 8
product = 1 #ცვლადი
for i in range(5, 11): #5 იდან 10-მე რიცხვები

    product *= i #ნამრავლების გაკეთება
print("ნამრავლები 5 იდან 10 ის ჩათვლით:", product) #ნამრავლი


