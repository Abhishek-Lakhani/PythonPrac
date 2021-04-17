name , age = input("Enter your name and age").split(" ")
name = (name.strip()).lower()
age = int(age)
if name[0] == 'a' and age >= 10:
    print("You can watch Movie")
else:
    print("you can not watch movie")