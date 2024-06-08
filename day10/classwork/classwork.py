name1 = int(input("enter attendance score:"))
print(name1)
if name1 < 80:
    print("issue certificate")
elif name1 >= 80:
    print("non issue certificate")

name2 = int(input('enter your age :'))
print(name2)
if name2 >= 18:
    print("you'r  allowed to watch r rated movies")
elif name2 < 18:
    print("you'r not allowed to watch r rated movies")