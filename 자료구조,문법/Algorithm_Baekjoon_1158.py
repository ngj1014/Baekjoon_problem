n, k = map(int, input().split())
lst = []
dap = []
for i in range(n):
    lst.append(i+1)

#num잡는게 포인트입니다.
num = k - 1

for i in range(n):
    if len(lst) > num :
        dap.append(lst.pop(num))
        num += (k-1)
    elif len(lst) <= num:
        num = num % len(lst)
        dap.append(lst.pop(num))
        num += (k-1)

print("<",', '.join(str(i) for i in dap),">",sep = '')
