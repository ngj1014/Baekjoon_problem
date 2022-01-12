from heapq import *
'''
n,m=map(int,input().split())
lst=[]
result=[]
for _ in range(m):
    lst.append(list(map(int,input().split())))

index=[0 for i in range(m)]

for _ in range(n):
    if index[0] == m:
        result.append(lst[1][index[1]])
        index[1]+=1
    elif index[1] == m:
        result.append(lst[0][index[0]])
        index[0] += 1

    else:
        if lst[0][index[0]] < lst[1][index[1]]:
            result.append(lst[0][index[0]])
            index[0] += 1
        elif lst[0][index[0]] > lst[1][index[1]]:
            result.append(lst[1][index[1]])
            index[1] += 1

print(result)

'''


'''
n,m=map(int,input().split())
lst=[]
heap=[]
result=[]
count=0
mini=32000
mem=0
for _ in range(m):
    lst.append(list(map(int, input().split())))

while True:
    if count==(n):
        break
    for i in range(m):
        heappush(heap, lst[i][0])

    result.append(heappop(heap))
    count+=1
    for i in range(m):
        if mini>lst[i][0]:
            mini=lst[i][0]
            mem=i

    lst[mem].pop(0)
    heap=[]

print(result)
'''
#위상정렬 : 순서가 정해져 있는 작업을 차례로 수행해야 할때 , 순서를 결정해주는 알고리즘이고
#시간 복잡도는 O(V+E)속도임.
#힙 = 우선순위 큐
#해답
import heapq
n,m=map(int,input().split())
array=[[] for i in range(n+1)]
indegree = [0] * (n+1)
heap=[]
result=[]
for _ in range(m):
    x,y=map(int , input().split())
    array[x].append(y)
    indegree[y]+=1
for i in range(1,n+1):
    if indegree[i]==0:
        heapq.heappush(heap,i)

result=[]
while heap:
    data=heapq.heappop(heap)
    result.append(data)
    for y in array[data]:
        indegree[y] -=1
        if indegree[y]==0:
            heapq.heappush(heap,y)

for i in result:
    print(i,end=' ')