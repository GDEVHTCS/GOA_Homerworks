#დავალება 1
for i in range(21):
    print(i)   #ნატურალური რიცხვების დაბეჭდვა 0 იდან 20 ის ჩათვლით

#დავალება 2
for i in range(10):
    print(i)   #პირველი ათი ნატურალური რიცხვის დაბეჭდვა

#დავალება 3
for i in range(101):
    if i % 2 == 0:
        print(i)


#დავალება 4
num1 = float(input("enter number:")) #მომხმარებელი შემოიტანს რიცხვს
if num1 > 0:
     print('number is positive') #თუ რიცხვი დადებითია დაწერს რომ დადებითია
elif num1 < 0:
    print("number is negative") #თუ რიცხვი არარის დადებითი დაწერს რომ ნეგატიურია
else:
    print("number is zero") #სხვა შემთხვევაში თუ რიცხვს შემოიტანს ნულს მაშინ  დაწერს რომ ნულია

#დავალება 5
user_age = int(input("enter your age:")) #მომხმარებელი შემოიტანს ასაკს
if user_age >= 18: 
    print('you are adult') # თუ დაწერს 18ს ან მეტს ის არის სრულწლოვანი
if user_age < 18:
    print("you are virgin") #და თუ 18 ზე ნაკლებს ის არის არასრულწლოვანი

#დავალება 6
week = int(input("enter any week of the day:")) #მომხმარებელი შემოიტანს რიცხვს რის შედეგადაც მიიღებს კვირის დღეს 
if week == 1:
    print("Monday")  #კვირის დღეები განლაგებული რიცხვებით
elif week == 2:
    print("Tuesday")
elif week == 3:
    print("Wednesday")
elif week == 4:
    print("Thursday")
elif week == 5:
    print("Friday")
elif week == 6:
    print("Saturday")
elif week == 7:
    print("Sunday")
else:
    print("ERROR")