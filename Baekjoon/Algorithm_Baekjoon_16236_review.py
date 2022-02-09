from collections import deque

#N의 크기와 배열을 입력받음.
n=int(input())
lst=[]
for _ in range(n):
    lst.append(list(map(int, input().split())))

#시뮬레이션을 확인하기위해서 좌우상하의 방향을 설정하였다.
dx=[-1,1,0,0]
dy=[0,0,-1,1]

#start_row / start_col을 찾는 과정이다.
for i in range(n):
    for j in range(n):
        if lst[i][j]==9:
            lst[i][j]=0
            start_row,start_col = i , j
            break

#처음 아기상어의 사이즈
size = 2
#얼만큼 움직였는지 move_num 즉, 답이 될것이다.
move_num = 0
#먹을 물고기의 수를 체크하는 변수이다.
eat = 0

#bfs로 최단거리를 구하는 과정. 다시 복습한다. -> dfs는 스택, bfs는 queue를 이용한다.
while True:
    q=deque()
    #start_row,start_col의 의미는 쉽지만 3번째 인덱스는 움직인 횟수를 체크하기위해서 만든 것, 튜플로 만듬.
    q.append((start_row,start_col,0))
    #방문한 것 체크하는 배열
    visited = [[False] * n for _ in range(n)]
    flag=1e9
    #헛된 움직임은 체킹하지 않으려고 물고기 위치와 물고기 위치까지 오기위해 움직인 거리를 저장함.
    fish=[]

    while q:
        x,y,count = q.popleft()

        # queue과정이 끝나면 또 실행 되지말라고 만든 것.
        if count>flag:
            break

        for k in range(4):
            #식을 간단하게 하기위한 변수선언.
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


    #queue빠져 나오고서는 이것만 반복 할 것 이다.
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