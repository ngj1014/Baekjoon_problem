import sys
input = sys.stdin.readline

#n은 전구의 개수, m은 명령어 개수
n,m = map(int, input().split())
#n개의 전구의 상태
lst = list(map(int,input().split()))

for _ in range(m):
    a,b,c = map(int,input().split())
    if a == 1:
        lst[b-1] = c
    elif a == 2 :
        for i in range(b-1,c):
            if lst[i] == 0:
                lst[i]=1
            else:
                lst[i]=0
    elif a == 3 :
        for i in range(b - 1, c):
            lst[i] = 0
    elif a == 4 :
        for i in range(b-1,c):
            lst[i] = 1

#리스트 값만 출력.
print(*lst)
