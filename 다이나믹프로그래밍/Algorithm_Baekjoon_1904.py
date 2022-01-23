'''
동적프로그래밍 : 1번계산한 것은 또 계산하지 않음 -> 이를 메모이제이션이라함
->점화식을 세워야함.
'''
'''
import sys
n=int(sys.stdin.readline())
a,b = 1 , 2
if n==1:
    print(a)
elif n==2:
    print(b)
else:
    for _ in range(n-2):
        a,b = b, (a+b)%15746
    print(b)

'''

n=int(input())
dp=[0]*1000001
dp[1]=1
dp[2]=2

for i in range(3,n+1):
    dp[i]=(dp[i-2]+dp[i-1])%15746

print(dp[n])