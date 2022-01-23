'''
#연결 요소를 세는 것이다.
import sys
from collections import deque
read=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]
#테스트 케이스 수
test_case=int(input())
#가로길이, 세로길이, 배추의 개수
def bfs(graph,a,b):
    q=deque()
    q.append((a,b))
    graph[a][b]=0

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=0
                q.append((nx,ny))

    return


for _ in range(test_case):
    cnt = 0
    m, n, k = map(int, read().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        a,b=map(int, read().split())
        graph[b][a]=1

    for i in range(m):
        for j in range(n):
            if graph[j][i]==1:
                bfs(graph,j,i)
                cnt+=1
    print(cnt)

'''

#setrecursionlimit()를 사용해보자..
import sys
read=sys.stdin.readline
#보통 재귀는 1000번만 가능하지만 100000번까지 가능하게 만듬.
sys.setrecursionlimit(100000)

def dfs(x,y):
    visited[x][y]=1
    directions=[(-1,0),(1,0),(0,-1),(0,1)]
    for dx,dy in directions:
        nx,ny = x+dx,y+dy
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if array[nx][ny] and visited[nx][ny]==0:
            dfs(nx,ny)


for _ in range(int(input())):
    m,n,k=map(int, read().split())
    array=[[0]*m for _ in range(n)]
    visited=[[0]*m for _ in range(n)]
    for _ in range(k):
        y,x=map(int,read().split())
        array[x][y]=1
    result=0
    for i in range(n):
        for j in range(m):
            if array[i][j]==1 and visited[i][j]==0:
                dfs(i,j)
                result += 1

    print(result)