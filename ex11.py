number = input("Enter number more then 1 digit")
total = 0
for i in range(0,len(number)):
    total = total + int(number[i])

print(total) 
# for sum of each digit