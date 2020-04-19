n = int(input())
k = 0
g = 0
for i in range(1,n+1) :
    if i % 2 == 0:
        g += 1
    else :
        k += 1
print(k/(g+k))
