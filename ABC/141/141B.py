s = input()
a = 0
for i in range(0,len(s),2):
    if s[i] == 'L' :
        a += 1
for i in range(1,len(s),2):
    if s[i] == 'R':
        a += 1
if a == 0 :
    print('Yes')
else :
    print('No')