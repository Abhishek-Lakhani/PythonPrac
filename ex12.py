# take list as input and return number of sublist
def number_sublist(l):
    count = 0
    for i in l:
        
        if type(i) == list:
            count += 1
    return count
A = [1,[1,2,3],[5,6,7],5,5,5,5,5]
print(number_sublist(A)) 