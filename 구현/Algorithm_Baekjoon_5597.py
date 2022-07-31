#확실히 튜플 형식을 어려워함.
lst = []
result = []
dap = []
for i in range(30):
    result.append([i+1,False])

for _ in range(28):
    n=int(input())
    result[n-1][1] = True

for i in range(30):
    if result[i][1] == False:
        print(i+1)

