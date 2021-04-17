n = int(input())
a = set()
for i in range(0,n):
    x = int(input())
    a.add(x)    
b = list(a)
b.sort()
print(b[-2])
