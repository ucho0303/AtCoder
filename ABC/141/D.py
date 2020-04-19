import heapq
n,m = map(int,input().split())
a = list(map(lambda x: int(x)*(-1),input().split()))
a.sort(reverse=True)
heapq.heapify(a)
for i in range(m):
    x = -heapq.heappop(a)
    x //= 2
    heapq.heappush(a,-x)
print(-sum(a))
