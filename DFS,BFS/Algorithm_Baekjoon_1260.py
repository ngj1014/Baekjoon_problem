import sys
from collections import deque
read=sys.stdin.readline

#DFS는 재귀를 사용하여 푸는 것이다./스택 형식을 따른다.
def dfs(v):
    #visit_list:방문 리스트를 사용하는 것이다.
    visit_list[v]=1
    print(v,end=' ')
    for i in range(1,n+1):
        if visit_list[i] == 0 and graph[v][i] == 1:
            dfs(i)


#BFS는 재귀를 사용하지않고, QUEUE를 사용하는데 for문을 이용하여 풀면 된다. -> 최단 거리를 효과적으로 풀어낼 수있다.
def bfs(v):
    q=deque()
    q.append(v)
    visit_list2[v]=1
    while q:
        v=q.popleft()
        print(v,end=" ")
        for i in range(1,n+1):
            if visit_list2[i] ==0 and graph[v][i]==1:
                q.append(i)
                visit_list2[i] = 1
n,m,v=map(int, read().split())

graph=[[0]*(n+1) for _ in range(n+1)]

visit_list=[0]*(n+1)
visit_list2=[0]*(n+1)

for _ in range(m):
    a, b=map(int,read().split())
    graph[a][b]=graph[b][a]=1


dfs(v)
print()
bfs(v)

