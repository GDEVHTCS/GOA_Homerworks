#პირველი პროგრამა
numbers = [-10, 15, -3, 7, -8, 0, 14, -5]

positives = [] #positive numbers
negatives = []#negative numbers

for num in numbers:
    if num > 0:
        positives.append(num)  
    elif num < 0:
        negatives.append(num)  

print("positive numbers:", positives)#დაიბეჭდოს ჩვეულიებრივი რიცხვები
print("negative numbers:", negatives)#დაიბეჭდოს მინუს რიცხვები

#მეორე პროგრამა
names = ["andria", "giorgi", "ani", "luka", "vache", "daviti"] #სახელების სია

names_starting_with_a = [] #დაწყებული a ასოდან

for name in names:
    if name[0] == 'a':
        names_starting_with_a.append(name)

print("Names starting with 'a':", names_starting_with_a) #დაბეჭდვა მხოლოდ a დან დაწყებულის

#მესამე პროგრამა
webdevlopment= ["html", "javascript", "css", 'saas','pyton' ]
print(webdevlopment)
names = (input("enter any programs that are in list:"))
if names ==("html"):
    print("easy prgoram")
elif names ==("javascript"):
    print("hard language")
elif names ==("css"):
    print("easy program")
elif names ==('saas'):
    print("easy program")
elif names ==("pyton"):
    print("hard language")