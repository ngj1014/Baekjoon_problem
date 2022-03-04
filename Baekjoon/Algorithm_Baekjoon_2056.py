#위상 정렬 조심할 것은 순서가 정해져 있는 것 -> 같은 것을 포함한 순열처럼 기억하면 좋다.
#위상정렬은 사이클이 없어야한다. 또한 답이 1개만 있지않다. ,마지막으로 방향 그래프이다.
#비교문제: 14567(선수과목) -> dp이기도 하지만 위상정렬이기도하다.
#dp문제랑 위상정렬이랑 같이 엮일수 있음.

#대표적인 위상정렬 문제 : 2056번 문제.

import sys
input = sys.stdin.readline

n = int(input())
times = [0] * (n+1)
graph = {}
#lst의 1번쨰 해당작업시간 , 2번쨰는 선행관계의 개수 , 3번째는 선행관계의 번호
for i in range(1,n+1):
    lst=list(map(int, input().split()))
    times[i] = lst[0]
    if lst[1] == 0:
        continue
    for j in lst[2:]:
        if i in graph:
            graph[i].append(j)
        else:
            graph[i] = [j]

for i in range(1,n+1):
    if i in graph:
        time = 0
        for j in graph[i]:
            time = max(time, times[j])
        times[i] += time


print(max(times))

