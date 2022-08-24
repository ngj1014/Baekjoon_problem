n = int(input())
lst = list(map(int,input().split()))

dp = [0] * n
dp[0] = lst[0]
result = lst[0]
for i in range(1,n):
    if dp[i-1]+lst[i]>lst[i]:
        dp[i] = (dp[i-1]+lst[i])
        if result<=dp[i]:
            result=dp[i]

    else:
        dp[i] = lst[i]
        if result <= dp[i]:
            result = dp[i]

print(result)
