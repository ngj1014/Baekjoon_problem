#정수 n 입력받기
n = int(input().rstrip())

#모든 식량 정보 입력 받기
lst = list(map(int,input().split()))

dp = [0] * 100

#다이나믹 프로그래밍(Dynamic Programming) 진행 (bottom up)
dp[0] = lst[0]
dp[1] = max(lst[0],lst[1])
for i in range(2,n):
    dp[i] = max(dp[i-1],dp[i-2]+lst[i])

print(dp[n-1])