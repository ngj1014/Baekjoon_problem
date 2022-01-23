'''
최단 경로는 못구한 코드이다.
import sys
from collections import deque
read=sys.stdin.readline
second=1001
def bfs(v):
    global result
    result = 1
    q=deque()
    q.append(v)
    visited_lst=[0]*(n+1)
    visited_lst[v]=1
    while q:
        v=q.popleft()
        for i in range(1, n + 1):
            if visited_lst[i] == 0 and graph[v][i] == 1:
                result += 1
                q.append(i)
                visited_lst[i] = 1

    return result

test_case=int(read())
for _ in range(test_case):
    n,d,c=map(int, read().split())
    graph=[[0]*(n+1) for _ in range(n+1)]
    sec_graph=[[0]*(n+1) for _ in range(n+1)]

    for _ in range(d):
        a,b,s=map(int, read().split())
        graph[b][a] = 1
        sec_graph[b][a] = s

    print(bfs(c),end=' ')
'''

import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    heap_data= []
    heapq.heappush(heap_data,(0,start))
    distance[start]=0
    while heap_data:
        dist,now=heapq.heappop(heap_data)
        if distance[now]< dist:
            continue
        for i in adj[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(heap_data,(cost,i[0]))


for _ in range(int(input())):
    n,m,start = map(int, input().split())
    adj = [[] for i in range(n+1)]
    distance = [1e9] * (n+1)
    for _ in range(m):
        x,y,cost=map(int, input().split())
        adj[y].append((x, cost))

    dijkstra(start)
    count=0
    max_distance=0
    for i in distance:
        if i!=1e9:
            count+=1
            if i > max_distance:
                max_distance = i

    print(count, max_distance)