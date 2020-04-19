h,a = map(int,input().split())
for i in range(10010):
    if h <= a*i:
        print(i)
        break