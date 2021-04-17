n = input("Enter number of more then 1 digit")
total = 0
i = 0
while i <= (len(n)-1):
    total = total +int(n[i])
    i += 1
print(total)