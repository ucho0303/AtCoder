n = int(input())
h = list(map(int,input().split()))
a,b = 0,0
C = [0]*n
for i in range(n-1):
  if h[i]>=h[i+1]:
    a+=1
  else:
    C[b]=a
    b+=1
    a=0
C[b]=a
print(max(C))