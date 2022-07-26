import sys
from itertools import combinations
input = sys.stdin.readline

n,m = map(int, input().split())
ice = [[False for _ in range(n)] for _ in range(n)]

#True라는 것은 조합이 안맞는다는 뜻.
for i in range(m):
    i1,i2 = map(int, input().split())
    ice[i1-1][i2-1] = True
    ice[i2-1][i1-1] = True

result=0

#i값에는 [a,b,c]형태가 들어가 있는데 [a,b],[a,c],[b,c]만 비교해보면된다. 없으면 없는 것. 왜냐하면 combination은 permutation이랑다름.
for i in combinations(range(n),3):
    if ice[i[0]][i[1]] or ice[i[0]][i[2]] or ice[i[1]][i[2]]:
        continue
    result+=1

print(result)

