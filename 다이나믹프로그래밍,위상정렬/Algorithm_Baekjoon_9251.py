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
'''

#재귀 이용하는 방법...
import sys
sys.setrecursionlimit(10**7)

def sol(i, j):

    if i < 0 or j < 0:
        return 0

    if d[i][j] >= 0:
        return d[i][j]

    if s1[i] == s2[j]:
        d[i][j] = 1 + sol(i-1, j-1)
    else:
        d[i][j] = max(sol(i-1, j), sol(i, j-1))

    return d[i][j]

s1, s2 = input().rstrip(), input().rstrip()
d = [[-1]*1000 for _ in range(1000)]
print(sol(len(s1)-1, len(s2)-1))
