import sys
sys.setrecursionlimit(10**5)
read=sys.stdin.readline
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

#N은 전체 행렬의 개수를 만들기위한 입력 값(2^N X 2^N핼렬) / C는 단계 몇번 출력할 것인가.
N,C = map(int, read().split())
N = 2 ** N
#얼음을 행렬로 입력받음. -> 각위치의 얼음을 입력
ice=[list(map(int, read().split())) for _ in range(N)]

#L의 입력값에 따라 로테이션이 이루어 짐.(서칭이 가능한 부분.)
for L in list(map(int, read().split())):
    #회전시키는 방법
    l=2**L
    for x in range(0, N, l):
        for y in range(0, N, l):
            tmp = [ice[i][y:y+l] for i in range(x, x+l)]
            for i in range(l):
                for j in range(l):
                    #회전 시키는 점화식(90도) -> 2번하면 180도 -> 3번하면 270도 회전
                    ice[x+j][y+l-1-i] = tmp[i][j]


    #인접한 얼음 카운팅
    cnt = [[0] * N for i in range(N)]
    for x in range(0, N):
        for y in range(0, N):
            for d in direction:
                nx, ny = x+d[0], y+d[1]
                if 0 <= nx < N and 0 <= ny < N and ice[nx][ny]:
                    cnt[x][y] += 1

    #얼음 제거 (제일 중요) -> 문장이 어려운 경우.
    for x in range(N):
        for y in range(N):
            #시발. 인접한 칸이 3개 미만이여야지 얼음 제거!
            if ice[x][y]>0 and cnt[x][y]<3:
                ice[x][y] -= 1

print(sum(sum(i) for i in ice))

def dfs(x,y):
    ret = 1
    ice[x][y] = 0
    for d in direction:
        nx,ny = x+d[0], y+d[1]
        if 0 <= nx < N and 0 <= ny < N and ice[nx][ny]:
            ret += dfs(nx, ny)
    return ret

#가장 큰 덩어리
ans = 0
for x in range(N):
    for y in range(N):
        if ice[x][y] > 0:
            ans = max(ans, dfs(x,y))

print(ans)


'''
import sys
sys.setrecursionlimit(10 ** 5)
dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

n, q = map(int, input().split())
n = 2 ** n
ice = [list(map(int, input().split())) for _ in range(n)]

for L in list(map(int, input().split())):
    # 회전
    k = 2 ** L
    for x in range(0, n, k):
        for y in range(0, n, k):
            tmp = [ice[i][y:y + k] for i in range(x, x + k)]
            for i in range(k):
                for j in range(k):
                    ice[x + j][y + k - 1 - i] = tmp[i][j]

    # 인접한 얼음 카운팅
    cnt = [[0] * n for i in range(n)]
    for x in range(0, n):
        for y in range(0, n):
            for d in dir:
                nx, ny = x + d[0], y + d[1]
                if 0 <= nx < n and 0 <= ny < n and ice[nx][ny]:
                    cnt[x][y] += 1
    # 얼음 제거
    for x in range(0, n):
        for y in range(0, n):
            if ice[x][y] > 0 and cnt[x][y] < 3:
                ice[x][y] -= 1

# 남아있는 얼음의 합
print(sum(sum(i) for i in ice))

# (x,y)가 속한 덩어리의 크기
def dfs(x, y):
    ret = 1
    ice[x][y] = 0
    for d in dir:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < n and 0 <= ny < n and ice[nx][ny]:
            ret += dfs(nx, ny)
    return ret

# 제일 큰 덩어리
ans = 0
for x in range(n):
    for y in range(n):
        if ice[x][y] > 0:
            ans = max(ans, dfs(x, y))
print(ans)
'''