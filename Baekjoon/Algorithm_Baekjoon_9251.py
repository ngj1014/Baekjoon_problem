'''틀린 풀이 -> 탐색으로 풀어볼려고함
import sys
lst=input()
lst_2=input()
n=len(lst)
m=len(lst_2)
count=0
dp=[0 for i in range(n)]
for i in range(n):
    result=0
    count=0
    for j in range(i,n):
        for k in range(count,m):
            if lst[j]==lst_2[k]:
                result+=1
                count+=1
                break
        break
    dp[i]=result

print(max(dp))
'''

x=input()
y=input()

dp=[[0] * (len(y)+1) for _ in range(len(x)+1)]

for i in range(1,len(x)+1):
    for j in range(1,len(y)+1):
        if x[i-1]==y[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i][j-1],dp[i-1][j])

print(dp[len(x)][len(y)])
