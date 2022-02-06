n, m = map(int, input().split())

lst = []

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
d=[]
s=[]
temp=[]

for _ in range(n):
    lst.append(list(map(int, input().split())))


for i in range(m):
    temp.append(list(map(int, input().split())))


for i in range(m):
    d.append(temp[i][0])
    s.append(temp[i][1])

#방향: 1번:왼쪽/2번: 왼쪽 위 대각선/3번: 위쪽/4번: 오른쪽 위 대각선/5번: 오른쪽/6번: 오른쪽아래 대각선/7번: 아래/8번: 왼쪽 아래 대각선
start = [[n-1, 0], [n-1, 1],[n-2, 0], [n-2, 1]]
index=0

while index<m:
    check = [[False] * n for _ in range(n)]
    leng=len(start)
    clouds = []
    if d[index] == 1:
        for i in range(leng):
            clouds.append([start[i][0]+dx[0]*s[index], start[i][1]+dy[0]*s[index]])
        index+=1
    elif d[index] == 2:
        for i in range(leng):
            clouds.append([start[i][0]+dx[1]*s[index], start[i][1]+dy[1]*s[index]])
        index+=1
    elif d[index] == 3:
        for i in range(leng):
            clouds.append([start[i][0]+dx[2]*s[index], start[i][1]+dy[2]*s[index]])
        index+=1
    elif d[index] == 4:
        for i in range(leng):
            clouds.append([start[i][0]+dx[3]*s[index], start[i][1]+dy[3]*s[index]])
        index+=1
    elif d[index] == 5:
        for i in range(leng):
            clouds.append([start[i][0]+dx[4]*s[index], start[i][1]+dy[4]*s[index]])
        index+=1
    elif d[index] == 6:
        for i in range(leng):
            clouds.append([start[i][0]+dx[5]*s[index], start[i][1]+dy[5]*s[index]])
        index+=1
    elif d[index] == 7:
        for i in range(leng):
            clouds.append([start[i][0]+dx[6]*s[index], start[i][1]+dy[6]*s[index]])
        index+=1
    elif d[index] == 8:
        for i in range(leng):
            clouds.append([start[i][0]+dx[7]*s[index], start[i][1]+dy[7]*s[index]])
        index+=1


    for i in range(leng):
        while clouds[i][0]<0 or clouds[i][1]<0:
            if clouds[i][0] < 0:
                clouds[i][0] += n
            if clouds[i][1] < 0:
                clouds[i][1] += n
        while clouds[i][0]>n-1 or clouds[i][1]>n-1:
            if clouds[i][0] > n-1:
                clouds[i][0] -= (n)
            if clouds[i][1] > n-1:
                clouds[i][1] -= (n)


    for i in range(leng):
        check[clouds[i][0]][clouds[i][1]]=True

    for i in range(leng):
        lst[clouds[i][0]][clouds[i][1]] += 1


    for i in range(leng):
        for j in range(4):
            if 0<=clouds[i][0]+dx[2*j+1]<n :
                if 0<=clouds[i][1]+dy[2*j+1]<n:
                    if lst[clouds[i][0]+dx[2*j+1]][clouds[i][1]+dy[2*j+1]]!=0:
                        lst[clouds[i][0]][clouds[i][1]]+=1

    start=[]
    for i in range(n):
        for j in range(n):
            if lst[i][j] >= 2 and check[i][j]==False:
                start.append([i,j])
                lst[i][j]-=2



sum=0
for i in range(n):
    for j in range(n):
        sum+=lst[i][j]

print(sum)