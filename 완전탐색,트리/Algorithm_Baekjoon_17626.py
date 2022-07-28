import sys
input = sys.stdin.readline

n = int(input())

dap = 1
for i in range(1,222):
    if n == i*i:
        print(dap)
        exit(0)

dap = 2
for i in range(1,222):
    for j in range(1,222):
        if n == (i*i + j*j):
            print(dap)
            exit(0)

dap = 3
for i in range(1,222):
    for j in range(1,222):
        for k in range(1,222):
            if n == (i*i + j*j + k*k):
                print(dap)
                exit(0)


dap=4
print(dap)
