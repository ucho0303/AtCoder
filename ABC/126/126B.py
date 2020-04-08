n = input()
a = int(n[:2])
b = int(n[2:])
x = 0 < a <= 12
y = 0 < b <= 12
if x and y :
    print('AMBIGUOUS')
elif not x and y:
    print('YYMM')
elif x and not y:
    print('MMYY')
else:
    print('NA')