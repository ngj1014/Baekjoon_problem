
import sys
input = sys.stdin.readline

n = int(input())
lst = []


for _ in range(n):
    start,end = map(int,input().split())
    lst.append([start,end])

lst.sort()
room=0
index=0
index_2=0
for i in range(1,lst[n-1][0]):
    if index==n:
        break

    if i == lst[index][0]:
        room+=1
        index+=1

    if i==lst[index_2][1]:
        room-=1
        index_2+=1

print(room)

'''
import heapq
n = int(input())

q = []

for i in range(n):
    start, end = map(int, input().split())
    q.append([start, end])

q.sort()

room = []
heapq.heappush(room, q[0][1])

for i in range(1, n):
    if q[i][0] < room[0]: # 현재 회의실 끝나는 시간보다 다음 회의 시작시간이 빠르면
        heapq.heappush(room, q[i][1]) # 새로운 회의실 개설
    else: # 현재 회의실에 이어서 회의 개최 가능
        heapq.heappop(room) # 새로운 회의로 시간 변경을 위해 pop후 새 시간 push
        heapq.heappush(room, q[i][1])

print(len(room))
'''