#rotation완성

#n은 홀수
n = int(input())

chess=[]

#시뮬레이션을 위한 dx,dy:좌,하,우,상
dx=[0, 1, 0, -1]
dy=[-1, 0, 1, 0]

#좌하-우상으로 움직이나 좌하1번/우상2번/좌하3번/우상4번 이런식으로 ->(count//2 + 1)방식이용. ->count는 1씩증가하면서 //count -1 일때 종료
count=0
for _ in range(n):
    chess.append(list(map(int, input().split())))

row, col = n//2, n//2
#0이 되면 멈춰
brk_num=1
while True:
    if brk_num==0:
        break
    for i in range(4):
        if row < 0 or col < 0 or row > n - 1 or col > n - 1:
            brk_num=0
            break
        for j in range(count//2 + 1):
            print([row, col])
            row = row + dx[i]
            col = col + dy[i]
        count+=1


#모래 흩날리기 방법. 10g 이상은 못넘긴