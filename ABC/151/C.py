n,m = map(int,input().split())
WA = [0]*n
AC  = [0]*n
wa = 0
for i in range(m):
    x = input().split()
    x[0] = int(x[0])
    if x[1] == 'WA' and AC[x[0]-1] == 0:
        WA[x[0]-1] += 1
    elif x[1] == 'AC' and AC[x[0]-1] == 0:
        AC[x[0]-1] += 1
        wa += WA[x[0]-1]
print(sum(AC),wa)        
