import sys
from collections import deque

input = sys.stdin.readline
lst = list(input())
stack = []
length = len(lst)
answer = 0
tmp = 1

for i in range(length-1):
    if lst[i] == '(':
        stack.append(lst[i])
        tmp *= 2

    elif lst[i] == '[':
        stack.append(lst[i])
        tmp *= 3

    elif lst[i] == ')':
        #중요 부분
        if not stack or stack[-1] == '[':
            answer = 0
            break
        if lst[i-1] == '(':
            answer += tmp

        stack.pop()
        tmp //= 2
    elif lst[i] == ']':
        #중요 부분
        if not stack or stack[-1] == '(':
            answer=0
            break
        if lst[i-1] == '[':
            answer += tmp
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(answer)