#입력받기
n,m,k=map(int, input().split())
lst=[]

for _ in range(m):
    r,c,m,s,d = list(map(int, input().split()))
    lst.append([r,c,m,s,d])

chess_pan = [[[] for _ in range(n)] for _ in range(n)]

#시뮬레이션 구현하기 위해서
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]

#이동횟수
for _ in range(k):
    while lst:
        cr,cc,cm,cs,cd = lst.pop(0)
        #중요) 1행이 n번행과 연결 , 1열이 n번 열과 연결
        nr = (cr + cs * dx[cd]) % n
        nc = (cc + cs * dy[cd]) % n
        chess_pan[nr][nc].append([cm,cs,cd])

    #2개이상인지 체크하자.
    for r in range(n):
        for c in range(n):
            #2개이상인지 체스판의 길이 체크 -> 길이 체크하려고 3차원 배열 선언.//처음시도는 count로 하려하였으나, len이 편하다.
            if len(chess_pan[r][c]) > 1:
                sum_m, sum_s, cnt_odd, cnt_even, cnt = 0,0,0,0,len(chess_pan[r][c])
                while chess_pan[r][c]:
                    m,s,d = chess_pan[r][c].pop(0)
                    sum_m += m
                    sum_s += s
                    if d%2 == 1:
                        cnt_odd +=1
                    else:
                        cnt_even +=1
                if cnt_odd == cnt or cnt_even ==cnt:
                    nd = [0,2,4,6]
                else:
                    nd = [1,3,5,7]

                if sum_m // 5:
                    for d in nd:
                        lst.append([r,c,sum_m//5,sum_s//cnt,d])
            #1개인 경우
            if len(chess_pan[r][c]) == 1:
                lst.append([r,c]+chess_pan[r][c].pop())

print(sum([f[2] for f in lst]))