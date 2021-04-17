if __name__ == '__main__':
    name = []
    score = []
    for _ in range(int(input())):
        name.append(input("name"))
        score.append(float(input("score")))
re = score.index(score(min))
name.pop(re)
score.pop(re)
n = score.index(score(min))
print(name[n])
if score.count(score(min)) > 1:
    for i in range(score.count(score(min))):
        global n = score.index(score(min,n))
        print(name[n])
