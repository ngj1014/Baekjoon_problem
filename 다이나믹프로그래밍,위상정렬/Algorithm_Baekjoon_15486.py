n = int(input())
day = [0]
value = [0]
dp = [0] * (n+2)
for _ in range(n):
    a,b = map(int, input().split())
    day.append(a)
    value.append(b)


for i in range(1,n+1):
    if dp[i]<dp[i-1]:
        dp[i] = dp[i-1]
    if i + day[i] <= n+1:
        if dp[i+day[i]] < dp[i] + value[i]:
            dp[i+day[i]] = dp[i] + value[i]

print(max(dp))



'''
완전 탐색
for i in range(n-1,-1,-1):
    num = 0
    for j in range(i+1,n):
        if dp[j] == 0:
            num+=1
        else:
            break

    if lst[i][0] - 1 <= num:
        dp[i] = max(dp)
        dp[i] += lst[i][1]

print(max(dp), end = '')
'''
