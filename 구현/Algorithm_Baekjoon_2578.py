import sys
input = sys.stdin.readline

#12번은외쳐야 답이나온다는 사실을 알아라.

def chk(k):
    flag = False
    for i in range(5):
        if flag == False:
            for j in range(5):
                if c_lst[i][j] == k:
                    lst[i][j] = True
                    flag = True
                    break

def bing_go(k):
    num=0
    #행에서 빙고
    for i in range(5):
        if lst[i][0] == True and lst[i][1] == True and lst[i][2] == True and lst[i][3] == True and lst[i][4] == True:
            num+=1
    #열에서 빙고
    for i in range(5):
        if lst[0][i] == True and lst[1][i] == True and lst[2][i] == True and lst[3][i] == True and lst[4][i] == True:
            num+=1

    #오른쪽 대각선 아래로
    if lst[0][0] == True and lst[1][1] == True and lst[2][2] == True and lst[3][3] == True and lst[4][4] == True:
        num+=1
    #왼쪽 대각선 아래로
    if lst[0][4] == True and lst[1][3] == True and lst[2][2] == True and lst[3][1] == True and lst[4][0] == True:
        num+=1

    if num>=3:
        print(k)
        exit(0)




global c_lst
global s_lst
global lst

c_lst = []
s_lst = []

lst = [[False] * 5 for _ in range(5)]
for _ in range(5):
    c_lst.append(list(map(int,input().split())))

for _ in range(5):
    s_lst.append(list(map(int,input().split())))




for i in range(5):
    for j in range(5):
        # 빙고 체크하기
        chk(s_lst[i][j])
        bing_go(i*5 + (j+1))



