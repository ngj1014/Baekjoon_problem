#로프 문제
import sys
n=int(sys.stdin.readline())
mylist=[int(sys.stdin.readline()) for i in range(n)]
mylist.sort()
result=0
for i in range(n):
    if result<n*mylist[i]:
        result=n*mylist[i]
        n-=1
    else:
        n-=1

print(result)
