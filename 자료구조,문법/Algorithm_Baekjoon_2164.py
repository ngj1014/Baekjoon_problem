from collections import deque
n=int(input())
lst = []
q = deque(lst)

for i in range(1,n+1):
    q.append(i)


while (1):
    if len(q) == 1:
        print(q[0])
        break
    else:
        q.popleft()
        q.append(q.popleft())
