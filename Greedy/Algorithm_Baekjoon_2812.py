'''
import sys
n,k = list(map(int, input().split()))

number=int(input())

lst=[]
for i in range(1,n+1):
    lst.append(number//10**(n-i))
    number=number%(10**(n-i))


count=0
dap=[]
dap.append(lst[n - 1])
i=1
while True:
    if count == n-k-1:
        break
    if lst[n-1-i]>dap[count]:
        dap.append(lst[n-1-i])
        count += 1
        i+=1
    else:
        i+=1


dap.reverse()
print(dap)


result=0
print(result)
'''

'''
import sys

N, K = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().strip()))

result = []
delNum = K

for i in range(N):
    while delNum > 0 and result:
        if result[len(result) - 1] < nums[i]:
            result.pop()
            delNum -= 1
        else:
            break
    result.append(nums[i])

for i in range(N - K):
    print(result[i], end="")
'''

