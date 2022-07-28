import sys
from itertools import permutations
input = sys.stdin.readline

lst=[]
result = []
n=int(input())
k=int(input())
for _ in range(n):
    lst.append(int(input()))

for i in permutations(lst,k):
    temp = ''.join(map(str,i))
    result.append(temp)

print(len(list(set(result))))