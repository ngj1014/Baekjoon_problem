n,k=map(int,input().split())
lst=[]
for _ in range(n):
    lst.append(int(input()))

dp=[0]*(k+1)

dp[0] = 1


#1원으로 만들수 있는 것은 1개씩이다. (1원,2원)으로 만들수 있는 것은 f(k)+f(k-2)
for i in lst:
    for j in range(i,k+1):
        dp[j]+=dp[j-i]

print(dp[k])