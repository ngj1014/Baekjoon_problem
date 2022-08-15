from collections import deque

lst = input()
length = len(lst)
result = 0
flag = False
stack = []
q=deque(stack)

for i in range(length):
    if lst[i] == '(':
        q.append(lst[i])
    else:
        if lst[i-1] == '(':
            q.pop()
            result+=len(q)
        else:
            q.pop()
            result+=1


print(result)