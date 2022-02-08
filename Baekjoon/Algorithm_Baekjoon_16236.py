#bfs로 최단 거리를 구하는 것이 포인트 -> 나는 길이 막혀있는 것을 제외한 코드는 구현 하였으나. (즉, 1,2,3,4 코드는 해결)
from collections import deque

n=int(input())
lst=[]
for _ in range(n):
    lst.append(list(map(int, input().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

#start_row / start_col을 찾자.
for i in range(n):
    for j in range(n):
        if lst[i][j]==9:
            lst[i][j]=0
            start_row,start_col = i , j
            break

size = 2
move_num = 0
eat = 0

while True:
    q=deque()
    q.append((start_row,start_col,0))
    visited = [[False] * n for _ in range(n)]
    flag=1e9
    fish=[]
    while q:
        x,y,count = q.popleft()

        if count>flag:
            break

        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if lst[nx][ny] >size or visited[nx][ny]:
                continue

            if lst[nx][ny] !=0 and lst[nx][ny]<size:
                fish.append((nx,ny,count+1))
                flag=count
            visited[nx][ny]=True
            q.append((nx,ny,count+1))

    if len(fish)>0:
        fish.sort()
        x,y,move = fish[0][0],fish[0][1],fish[0][2]
        move_num += move
        eat += 1
        lst[x][y]=0
        if eat == size:
            size+=1
            eat=0
        start_row,start_col = x,y
    else:
        break

print(move_num)