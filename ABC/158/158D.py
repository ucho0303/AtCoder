s1 = input()
s2 = s1[::-1]
q = int(input())
x = 0
for i in range(q):
    query = input().split()
    if query[0] == '1':
        x += 1
    else :
        y = x + int(query[1])
        if y % 2 == 0:
            s1 = s1 + query[2]
            s2 = query[2] + s2
        else :
            s1 = query[2] + s1
            s2 = s2 + query[2]
if x % 2 == 0:
    print(s1)
else :
    print(s2)