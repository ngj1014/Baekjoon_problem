import sys
input = sys.stdin.readline

n = int(input())
'''
#그리디로 풀었더니 바로 실패.
result = 0
while True:
    if n == 1:
        print(result,end='')
        break
    else:
        if n%3 == 0:
            n//=3
            result+=1
        elif n%2 == 0:
            n//=2
            result+=1
        else:
            n-=1
            result+=1
'''

dp = [0] * (n+1)
for i in range(2,n+1):
    dp[i] = dp[i-1] + 1
    if i%2 == 0:
        dp[i] = min(dp[i],dp[i//2]+1)
    if i%3 == 0:
        dp[i] = min(dp[i],dp[i//3]+1)

print(dp[n])