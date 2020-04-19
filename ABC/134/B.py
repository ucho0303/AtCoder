n,d = map(int,input().split())
x = 1 + d*2
for i in range(21):
    if x*i >= n:
        print(i)
        break