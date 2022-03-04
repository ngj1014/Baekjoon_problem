import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [1] * n
flag = [0] * n
lst=[]
for _ in range(m):
    lst.append(tuple(map(int, input().split())))

lst=sorted(lst, key=lambda x:x[1])

for i in lst:
    a,b = i
    if flag[b-1] == 0:
        flag[b-1] = dp[a-1]
        dp[b-1]=dp[b-1]+dp[a-1]
    else:
        if dp[a-1] < flag[b-1]:
            pass
        else:
            dp[b-1]=dp[b-1]-flag[b-1]+dp[a-1]
            flag[b-1]=dp[a-1]





for i in range(len(dp)):
    print(dp[i], end=' ')
