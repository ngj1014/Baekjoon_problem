#은행문제
n = input()
p = list(map(int, input().split()))
p.sort()
result = []
count = 0
dap = 0
for i in p:
    count += i
    result.append(count)
for i in result:
    dap += i

print(dap)
