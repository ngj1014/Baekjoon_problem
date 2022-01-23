#곡 개수: N개
#볼륨리스트: V(list) , V[i]:i번째 곡을 연주하기 전에 바꿀수 있는 볼륨, 현재볼륨 P, 그 다음 볼륨은 P-V[i] , P+V[i]
#0보다 작은 볼륨은 없고, M보다 큰 볼륨도 없다.
# N,S,M <-곡의 개수,스타트 볼륨,최대 볼륨

n,s,m=map(int, input().split())
v=list(map(int, input().split()))

dp=[[0]*(m+1) for _ in range(n+1)]
print(dp)
dp[0][s]=1
for i in range(1,n+1):
    for j in range(m+1):
        if dp[i-1][j]==0:
            continue
        if j - v[i-1]>=0:
            dp[i][j-v[i-1]]=1
        if j + v[i-1]<=m:
            dp[i][j+v[i-1]]=1

result= -1
for i in range(m,-1,-1):
    if dp[n][i]==1:
        result=i
        break

print(result)