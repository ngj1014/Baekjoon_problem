'''
import sys
input=sys.stdin.readline
n=int(input())
A=[]

for i in range(n):
    A.append(list(map(int, input().split())))

A.sort()
count=0
distance = []
distance_2=0
for i in range(n):
    post_position = A[count][0]
    for j in range(n):
        if post_position == A[j][0]:
            continue
        else:
            distance_2 += (abs(A[j][0]-post_position) * A[j][1])

    distance.append(distance_2)
    count += 1
    distance_2=0

mini=1e10
for i in range(n):
    if mini>distance[i]:
        mini = distance[i]
        index = i


print(A[index][0])
'''


n=int(input())

info=[]
people=0

for i in range(n):
    x=list(map(int,input().split()))
    info.append(x)
    people+=x[1]

info=sorted(info)

mid=people//2

if (people%2)==1:
    mid+=1

count=0
for i,p in info:
    count+=p


    if count>=mid:
        print(i)
        break