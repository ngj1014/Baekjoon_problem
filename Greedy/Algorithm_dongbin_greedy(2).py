''' 큰 수의 법칙'''
n, m, k = map(int, input().split()) #data 갯수,#더할 갯수,#최대 연속수
data = list(map(int, input().split()))
data.sort()
first = data[n-1]
second = data[n-2]
dap = 0
q = int(m/(k+1))
r = int(m%(k+1))
for i in range(q):
    for j in range(k):
        dap += first
    dap += second

for i in range(r):
    dap += first

print(dap)
