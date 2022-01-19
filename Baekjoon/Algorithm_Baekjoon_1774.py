'''사이클을 생각하지 않음. 최단 거리로 연결 할 것인데 사이클 생기는 경우가 테스트 케이스에 없어서..
import sys
import math
read=sys.stdin.readline
n,m = map(int ,read().split())
lst=[]
connect_lst=[]
distance_lst=[]
result=0
for _ in range(n):
    a,b = map(int, read().split())
    lst.append((a,b))


for _ in range(m):
    a,b = map(int , read().split())
    connect_lst.append((a,b))

count=0
count_2=0
for i in range(n):
    for j in range(i,n):
        if i != j:
            if count_2<m:
                if i+1 == connect_lst[count_2][0] and j+1 == connect_lst[count_2][1]:
                    count_2+=1
                    continue
            dap = math.sqrt((lst[i][0] - lst[j][0]) ** 2 + (lst[i][1] - lst[j][1]) ** 2)
            distance_lst.append(dap)
            count += 1


distance_lst = sorted(distance_lst)
for i in range(n-m-1):
    result += distance_lst[i]
print("%.2f" %result)
'''




import math
import sys
input=sys.stdin.readline

def get_distance(p1,p2):
    a=p1[0]-p2[0]
    b=p1[1]-p2[1]
    return math.sqrt((a*a)+(b*b))

def get_parent(parent,n):
    if parent[n]==n:
        return n
    return get_parent(parent,parent[n])

def union_parent(parent,a,b):
    a=get_parent(parent,a)
    b=get_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

def find_parent(parent,a,b):
    a=get_parent(parent,a)
    b=get_parent(parent,b)
    if a == b:
        return True
    else:
        return False


edges=[]
parent={}
locations=[]

n,m = map(int, input().split())

for _ in range(n):
    x, y = map(int, input().split())
    locations.append((x,y))

length = len(locations)

for i in range(length -1):
    for j in range(i+1,length):
        edges.append((i+1,j+1,get_distance(locations[i],locations[j])))

for i in range(1,n+1):
    parent[i]=i

for i in range(m):
    a, b =map(int, input().split())
    union_parent(parent,a,b)

edges.sort(key=lambda data:data[2])

result = 0

for a,b,cost in edges:
    if not find_parent(parent,a,b):
        union_parent(parent,a,b)
        result+=cost

print("%0.2f" %result)

