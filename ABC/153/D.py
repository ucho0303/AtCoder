h = int(input())
for i in range(50):
    if 2**i > h:
        print(2**i-1)
        break