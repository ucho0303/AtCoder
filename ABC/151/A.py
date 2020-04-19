import string
s = input()
x = string.ascii_letters
for i in range(len(x)):
    if x[i] == s:
        print(x[i+1])
        break