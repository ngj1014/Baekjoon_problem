#BFS: 큐 이용하기! // 큐에 삽입 한 후(출력)에 방문처리

from collections import deque

def BFS(graph, start, visited):
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

graph=[
    [],#index 1번부터 시작하려고
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False]*9

BFS(graph, 1, visited)