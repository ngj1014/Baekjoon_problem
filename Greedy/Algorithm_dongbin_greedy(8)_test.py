'''그리디 문제를 괜히 반례찾으려 ㄴㄴ'''
n = int(input())
mylist = list(map(int, input().split()))
mylist.sort()
dap = 1
for i in mylist:
    if dap<i:
        break
    dap+=i
print(dap)
