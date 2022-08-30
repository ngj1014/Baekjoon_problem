n = int(input())
lst = []
for _ in range(n-1):
    lst.append(list(map(int,input().split())))

k = int(input())
dp = [0] * n

if n==1:
    print(0)
    exit()
elif n==2:
    print(lst[0][0])
    exit()
#가장 큰 점프 배제한 것
dp[1] = lst[0][0]
dp[2] = min(lst[0][1], lst[0][0]+lst[1][0])

for i in range(3,n):
    dp[i] = min(dp[i-2]+lst[i-2][1],dp[i-1]+lst[i-1][0])

#가장 큰 점프 포함 / 그리고 dp2를 이용하여 복사.
res = dp[-1]
dp2 = dp[:]

for i in range(0,n-3):
    if dp[i]+k < dp[i+3]:
        dp2[i+3]=dp[i]+k
        for j in range(i+4,n):
            dp2[j] = min(dp[j],dp2[j-1]+lst[j-1][0],dp2[j-2]+lst[j-2][1])
        if dp2[-1]<res:
            res=dp2[-1]

print(res,end='')

