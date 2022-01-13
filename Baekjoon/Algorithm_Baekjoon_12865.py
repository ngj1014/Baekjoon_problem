#점화식을 잘 짜면, 동적프로그래밍을 잘 짤수 있다.

#난이도 (하) -> 꼭 기억하자./ 제일 자주 물어보는 문제임.

#시간 복잡도 O(nk)시간임
n,k = map(int , input().split())
dp=[[0] * (k+1) for _ in range(n+1)]

for i in range(1,n+1):
    weight,value=map(int,input().split())
    for j in range(1,k+1):
        if j<weight:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)
print(dp[n][k])