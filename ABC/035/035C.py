N,K = map(int,input().split())
a =  input().split()
for i in range(len(a)):
    a[i] = int(a[i])

consum = [0]
for i in range(N) :
    consum.append(consum[i]+a[i])

answer = 0
for i in range(N-K+1) :
    answer += consum[i+3] - consum[i]


print(answer)