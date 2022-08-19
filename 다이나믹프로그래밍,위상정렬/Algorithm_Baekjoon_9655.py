#대표적인 dp문제 -> 규칙성 찾기?
#1개남거나 3개남으면 승부가 결정난다. -> dp[i-1] == 1이거나 dp[i-3] == 1이면 결정

import sys
input = sys.stdin.readline
dp = [-1] * 1001
n = int(input())
dp[1] = 1
dp[2] = 0
dp[3] = 1

for i in range(4,n+1):
    if dp[i-1] or dp[i-3]:
        dp[i] = 0
    else:
        dp[i] = 1

if dp[n] == 0:
    print('CY')
else:
    print('SK')