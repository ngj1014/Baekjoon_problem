#테스트 케이스(Test Case) 입력
for tc in range(int(input())):
    #금광 정보 입력
    n,m = map(int, int().split())
    array = list(map(int, input().split()))

    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])
        index+=m

    for j in range(1,m):
        for i in range(n):
            #왼쪽위에서 오는경우
            if i==0: left_up = 0
            else: left_up =dp[i-1][j-1]
            #왼쪽아래서 오는경우
            if i==n-1 : left_down = 0;
            else: left_down = dp[i+1][j-1]
            #왼쪽에서 오는경우
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up,left_down,left)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])

    print(result)