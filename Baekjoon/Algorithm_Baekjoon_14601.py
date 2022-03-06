def isComplete(row,col,size):
    for i in range(row, row+size):
        for j in range(col,col+size):
            if showerRoom[i][j] != 0:
                return False
    return True

def tile(row,col,size):
    global tile_num
    #분할정복의 끝을 알리는 거니까 재귀 돌아가기 전에 시행
    if size == 2:
        tile_num += 1
        for i in range(row,row+size):
            for j in range(col,col+size):
                if showerRoom[i][j] == 0:
                    showerRoom[i][j] = tile_num
        return

    size //= 2
    tile_num += 1
    if isComplete(row,col,size):
        showerRoom[row+size-1][col+size-1] = tile_num
    if isComplete(row+size,col,size):
        showerRoom[row+size][col+size-1] = tile_num
    if isComplete(row,col+size,size):
        showerRoom[row+size-1][col+size] = tile_num
    if isComplete(row+size,col+size,size):
        showerRoom[row+size][col+size] = tile_num


    # 재귀 - 분할정복
    tile(row,col,size)
    tile(row+size,col,size)
    tile(row,col+size,size)
    tile(row+size,col+size,size)


#첫 번째 입력값은 바닥의 크기인데, 2^k값으로 받아야함.
k = 2 ** int(input())
#하수구의 위치.
drain = tuple(map(int, input().split()))

#채워놓기
showerRoom = [[0 for _ in range(k)] for _ in range(k)]

#타일의 왼쪽 아래가 (1,1) 위치이고, 오른쪽 위가 (2^k,2^k) 위치이다. ->따라서 col먼저 체크하기
showerRoom[k-drain[1]][drain[0]-1] = -1

tile_num = 0

tile(0, 0, k)

for line in showerRoom:
    print(*line)