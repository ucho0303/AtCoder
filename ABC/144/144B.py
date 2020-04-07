N = int(input())
y = 0
for a in range(1,10):
    for b in range(1,10) :
        if N == a*b :
            print('Yes')
            y += 1
            break
    if y != 0 :
        break
if y == 0 :
    print('No')