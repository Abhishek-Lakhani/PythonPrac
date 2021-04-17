# writing data to file

fileHandler = open('Abhi.txt','w')
x = int(input("how much line you want to enter"))
for i in range(x):
    string1 = input("YOur data")
    fileHandler.write(string1 + '\n')
fileHandler.close()