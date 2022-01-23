n,m=map(int, input().split())
lst=[]
count=0
count_2=0
for _ in range(n):
    lst.append(input())

for i in range(n):
    for j in range(m):
        if lst[i][j] == 'X':
            count+=1
            break

for i in range(m):
    for j in range(n):
        if lst[j][i] == 'X':
            count_2+=1
            break

dap=max(n-count,m-count_2)
print(dap)