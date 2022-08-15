#deque rotate사용하기에 딱 좋은 문제이다.
import sys
from collections import deque
input = sys.stdin.readline

n=int(input())
q = deque(enumerate(map(int,input().split())))
ans = []

while q:
    idx,paper = q.popleft()
    ans.append(idx+1)
    #rotate(-1): 시계반대방향 1칸 / rotate(1):시계방향으로 1칸
    #음수일 땐, 양수만들어야해서 -붙이고, 양수일땐,음수만들어야하니 -qn붙이고
    if paper>0:
        q.rotate(-(paper-1))
    elif paper<0:
        q.rotate(-paper)

print(*ans)