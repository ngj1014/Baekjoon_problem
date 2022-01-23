dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    global result
    #동일한 경우 1번만 계산하기위해 set자료형 이용
    q=set()
    q.add((x,y,array[x][y]))

    while q:
        x,y,step=q.pop()
        #가장 긴 이동거리를 저장
        result=max(result,len(step))

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if (0<=nx and nx<r and 0<=ny and ny<c and array[nx][ny] not in step):
                q.add((nx,ny,step+array[nx][ny]))




r,c=map(int,input().split())
array=[]
for _ in range(r):
    array.append(input())

result=0
bfs(0,0)
print(result)


