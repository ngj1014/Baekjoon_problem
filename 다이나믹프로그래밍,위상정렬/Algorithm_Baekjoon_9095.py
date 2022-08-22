for _ in range(int(input())):
    num = int(input())
    dp = [0]*(11)
    dp[0] = 1
    dp[1] = 2
    dp[2] = 4
    for i in range(3,11):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]


    print(dp[num-1])