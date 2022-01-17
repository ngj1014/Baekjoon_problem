'''
from collections import deque
result=0
def bfs(v):
    global result
    q=deque()
    q.append(v)
    lst[v]=1
    while q:
        v=q.popleft()
        for i in range(1,n+1):
            if lst[i]==0 and graph[v][i]==1:
                result += 1
                q.append(i)
                lst[i]=1

    print(result)


#컴퓨터의 수(정점의 수)
n=int(input())
#컴퓨터와 연결되어 있는 수(간선의 수)
m=int(input())
lst=[0]*(n+1)
graph=[[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=graph[b][a]=1

bfs(1)
'''

#DFS풀이
n=int(input())
m=int(input())
adj=[[] for _ in range(n+1)]
visited=[0]*(n+1)
count=0

for _ in range(m):
    x, y=map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

def dfs(now_pos):
    global count
    count+=1
    visited[now_pos]=1
    for next_pos in adj[now_pos]:
        if visited[next_pos]==1:
            dfs(next_pos)



dfs(1)
print(count-1)