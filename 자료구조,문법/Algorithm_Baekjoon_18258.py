import sys
from collections import deque
n = int(input())
lst = []
q = deque(lst)
for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        q.appendleft(command[1])
    elif command[0] == 'pop':
        if len(q) != 0:
            print(q.pop())
        else:
            print("-1")
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'empty':
        if len(q) == 0:
            print("1")
        else:
            print("0")
    elif command[0] == 'front':
        if len(q) != 0:
            print(q[-1])
        else:
            print("-1")
    elif command[0] == 'back':
        if len(q) != 0:
            print(q[0])
        else:
            print("-1")