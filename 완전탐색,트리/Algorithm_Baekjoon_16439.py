import sys
input = sys.stdin.readline

n,m = map(int, input().split())

lst = []
dap = 0
for _ in range(n):
    lst.append(list(map(int,input().split())))

for i in range(m):
    for j in range(m):
        for k in range(m):
            checking = 0
            if i != j and j != k and i != k:
                for l in range(n):
                    checking += max(lst[l][i],lst[l][j],lst[l][k])
                if dap<=checking:
                    dap=checking
print(dap)