'''
import sys
input = sys.stdin.readline

n = int(input())
lst=list(map(int, input().split()))

left = 0
right = n-1
maximum=0
while True:
    if right-left==1:
        break
    leng=right-left-1
    if lst[left]<lst[right]:
        k=lst[left]
        left+=1
    else:
        k=lst[right]
        right-=1

    dap=leng*k

    if dap>maximum:
        maximum=dap

print(maximum)

'''

'''윤수풀이'''

import sys
input = sys.stdin.readline

n = int(input())
d = list(map(int, input().split()))
s, e = 0, n-1
r = 0
while s < e:
    r = max(r, min(d[s], d[e])*(e-s-1))
    if d[s] <= d[e]:
        s += 1
    else:
        e -= 1
print(r)