'''
런타임 에러
import sys
input = sys.stdin.readline
n=int(input())
m=int(input())

board = [[0 for _ in range(n)] for _ in range(n)]

#오른쪽, 아래쪽, 왼쪽, 위쪽 순서
dr = [0,1,0,-1]
dc = [1,0,-1,0]

r = n//2
c = n//2
num = 1
len = 0

board[r][c] = num

while True:
    for i in range(4):
        for _ in range(len):
            r+=dr[i]
            c+=dc[i]
            num+=1
            board[r][c] = num
            if num == m:
                ans = [r+1,c+1]

    if r == c == 0:
        break
    r -= 1
    c -= 1
    len += 2

for i in range(n):
    print(*board[i])

print(*ans)
'''
n = int(input())
find = int(input())

snail = [[0] * n for i in range(n)]
value = 1
direc = 1
count = 1
xtemp = int((n - 1) // 2)
ytemp = int((n - 1) // 2)
snail[xtemp][ytemp] = value

while value != n * n:
    if (direc == 1):
        for i in range(count):
            value += 1
            xtemp -= 1
            snail[xtemp][ytemp] = value
            if (value == n*n):
                break

        direc = 2

    elif (direc == 2):
        for i in range(count):
            value += 1
            ytemp += 1
            snail[xtemp][ytemp] = value
        count += 1
        direc = 3

    elif (direc == 3):
        for i in range(count):
            value += 1
            xtemp += 1
            snail[xtemp][ytemp] = value

        direc = 4

    elif (direc == 4):
        for i in range(count):
            value += 1
            ytemp -= 1
            snail[xtemp][ytemp] = value
        count += 1
        direc = 1

for i in range(n):
    for j in range(n):
        print(snail[i][j], end=" ")
        if (snail[i][j] == find):
            save_x = i+1
            save_y = j+1
    print()

print(save_x, save_y)
