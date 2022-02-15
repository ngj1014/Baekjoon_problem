import sys

input= sys.stdin.readline
sys.setrecursionlimit(10**9)

n=int(input())
graph=[[] for _ in range(n+1)]

def dfs(x,weight):
    for i in graph[x]:
        a,b= i
        if distance[a] == -1:
            distance[a] = weight + b
            dfs(a,weight+b)

#트리를 구현 , 무방향 그래프이므로 양쪽 방향을 다 체크해줘야함.
for _ in range(n-1):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])


#1번노드에서 가장 먼 노드를 체크. 가장 깊지않아도됨. -> 나중에 반대쪽에 깊은 곳으로 들어갈 예정. // 방문 여부도 확인 가능하다.
distance = [-1] * (n+1)
distance[1] = 0
dfs(1,0)

#위에서 찾은 노드에 대한 가장 먼 노드를 찾는다.
start = distance.index(max(distance))
distance = [-1] * (n+1)
distance[start] = 0
dfs(start, 0)

print(max(distance))