import sys
input = sys.stdin.readline
dp = []
dp.append(0)
dp.append(1)

n = int(input())

for i in range(n-1):
    dp.append(dp[i]+dp[i+1])

print(dp[n])


