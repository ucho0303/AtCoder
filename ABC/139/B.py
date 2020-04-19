a,b = map(int, input().split())
for i in range(21) :
    if b <= 1 + a*i-i :
        print(i)
        break