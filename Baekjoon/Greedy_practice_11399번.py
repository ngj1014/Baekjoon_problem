#탐욕알고리즘은 sorting하고 그 다음에 데이터 처리하는 경우가 많다.
n=int(input())
array=list(map(int,input().split()))

array.sort()

result=0

for i in range(n):
    for j in range(i+1):
        result+=array[j]

print(result)
