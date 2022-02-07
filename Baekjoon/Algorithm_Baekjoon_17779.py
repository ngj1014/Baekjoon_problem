def gerry(n,lst,x,y,d1,d2):
    M=[[0 for _ in range(n)] for _ in range(n)]
    #5번영역 그림
    for i in range(d1+1):
        if not (0<=x+i<n and 0<=y-i <n):
            return -1
        M[y-i][x+i] = 5

    for i in range(d1+1):
        if not (0<=x+d2+i<n and 0<=y+d2-i<n):
            return -1
        M[y+d2-i][x+d2+i] = 5

    for i in range(d2+1):
        if not (0<=x+i<n and 0<=y+i<n):
            return -1
        M[y+i][x+i] = 5

    for i in range(d2+1):
        if not (0 <= x+d1+i < n and 0 <=y-d1+i<n):
            return -1
        M[y-d1+i][x+d1+i]=5



    #1,2,3,4영역 색칠하기.
    for c in range(x+d1+1):
        for r in range(y):
            if M[r][c]==5:
                break
            M[r][c]=1

    for r in range(y-d1+d2+1):
        for c in range(n-1,x+d1,-1):
            if M[r][c]==5:
                break
            M[r][c] = 2

    for c in range(x+d2+2):
        for r in range(n-1,y-1,-1):
            if M[r][c] ==5:
                break
            M[r][c] = 3

    for r in range(y-d1+d2+1,n):
        for c in range(n-1,x+d2-1,-1):
            if M[r][c] == 5:
                break
            M[r][c]=4


    #인구수 체크

    res=[0,0,0,0,0]
    for r in range(n):
        for c in range(n):
            if M[r][c] == 0 or M[r][c] == 5:
                res[0] += lst[r][c]
            else:
                res[M[r][c]] +=lst[r][c]

    return max(res) - min(res)








n=int(input())
lst=[]
for _ in range(n):
    lst.append(list(map(int, input().split())))

gerry(n,lst,1,3,2,2)
result=[]
for x in range(n):
    for y in range(n):
        for d1 in range(1,int(n*1.414)+1):
            for d2 in range(1,int(n*1.414)+1):
                element = gerry(n,lst,x,y,d1,d2)
                if element == -1:
                    break
                else:
                    result.append(element)

print(min(result))
