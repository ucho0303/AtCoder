x,y,a,b,c = map(int,input().split())
red = list(map(int,input().split()))
green = list(map(int,input().split()))
colorless = list(map(int,input().split()))
red.sort(reverse=True)
green.sort(reverse=True)
apple = red[:x] +  green[:y] + colorless
apple.sort(reverse=True)
print(sum(apple[:x+y]))