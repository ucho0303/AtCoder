n =int(input())
a = list(map(int,input().split()))
b = []
x = {}
def fx(x) :
    ans = 0
    for i in range(1,x):
        ans += i
    return ans
for i in a :
    if i in x :
        x[i] += 1
        if x[i] == 2:
            b.append(i)
    else :
        x[i] = 1
anskari = 0
for i in b :
    anskari += fx(x[i])
for i in a :
    if x[i] == 1:
        print(anskari)
    else :
        print(anskari - x[i] +1)
    
