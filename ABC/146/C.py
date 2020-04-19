a,b,x = map(int,input().split())
yes = 0
no = 10**9 + 1
while yes + 1 != no:
    y = int((yes + no)/2)
    if a*y + b*len(str(y)) <= x:
        yes = y
    else :
        no = y
print(yes)
