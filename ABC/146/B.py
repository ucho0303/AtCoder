N = int(input())
S = [*input()]

a = [chr(i) for i in range(65, 65+26)]
b = [chr(i) for i in range(65+N, 65+26)]
for i in range(N):
    b.append(a[i])

a_dict = {}
for i in range(len(a)) :
    a_dict[a[i]] = b[i]
for i in range(len(S)) :
    S[i] = a_dict[S[i]]

print(''.join(S))