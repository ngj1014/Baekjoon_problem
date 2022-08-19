import sys
import itertools

def factorial(n):
    num = 1
    for i in range(1,n+1):
        num*=i
    return num


input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    n,m = map(int, input().split())
    dap = factorial(m) // (factorial(n)*factorial(m-n))
    print(dap)
