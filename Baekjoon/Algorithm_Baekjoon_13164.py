import sys
input=sys.stdin.readline

n,k=map(int,input().split())

lst=list(map(int, input().split()))

lst.sort()

distance=[]
for i in range(1,n):
    distance.append(lst[i]-lst[i-1])

distance.sort(reverse=True)

for i in range(k-1):
    distance[i]=0


print(sum(distance))