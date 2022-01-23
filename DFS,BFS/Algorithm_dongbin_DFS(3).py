def DFS(graph, v, visited):
    print(v, end=' ') #스택에 넣기
    visited[v] = True #방문처리
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)

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

DFS(graph, 1, visited)