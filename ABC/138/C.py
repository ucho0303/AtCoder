n = int(input())
a = list(map(int, input().split()))
a.sort()
def Alchemy(x) :
    if len(x) == 1 :
        print(x[0])
    else :
        a = (x[0] + x[1])/2
        l = x[2:]
        l.insert(0,a)
        return Alchemy(l)

Alchemy(a)