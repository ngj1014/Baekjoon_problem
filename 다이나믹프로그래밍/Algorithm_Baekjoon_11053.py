import sys
n=int(sys.stdin.readline())
lst=list(map(int,input().split(' ')))
result=0
check=[]
dp=[0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if lst[i]>lst[j] and dp[i]<dp[j]:
            dp[i]=dp[j]
    dp[i]+=1

print(dp)
print(max(dp))


