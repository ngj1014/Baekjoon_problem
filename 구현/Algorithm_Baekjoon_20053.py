import sys
input = sys.stdin.readline

n=int(input())

for _ in range(n):
    t = int(input())
    lst = list(map(int,input().split()))
    print(min(lst),max(lst))