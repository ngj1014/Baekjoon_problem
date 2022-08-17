import sys
input = sys.stdin.readline

'''
n,m = map(int, input().split())
lst = set([input() for _ in range(n)])
dap = 0


for _ in range(m):
    k = input()
    if k in lst:
        dap+=1
print(dap)
'''

n,m = map(int, input().split())
d = dict()
dap = 0
for _ in range(n):
    s = input().rstrip()
    d[s] = 1

for _ in range(m):
    t = input().rstrip()
    if t in d:
        dap+=1

print(dap)