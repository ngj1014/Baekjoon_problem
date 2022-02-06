'''
n=int(input())
chess=[[0]*n for _ in range(n)]
lst=[]

for _ in range(n*n):
    lst.append(list(map(int, input().split())))




dx = [-1,1,0,0]
dy = [0,0,-1,1]


check=[False]*(n*n)


#while문 돌게하려고
count_3=0
start=0

#while문 만들어야함.
while start<9:
    count = [0] * (n * n)
    count_2 = [0] * (n * n)

    #1번조건
    index=0
    #2번조건
    index_2=0

    #i:row / j:col
    for i in range(n):
        for j in range(n):
            #조건1번
            for k in range(4):
                if 0<=i+dx[k]<n and 0<=j+dy[k]<n:
                    for l in range(1,5):
                        if chess[i+dx[k]][j+dy[k]] == lst[start][l]:
                            if check[index] == True:
                                continue
                            count[index]+=1
            index+=1

            for k in range(4):
                if 0<=i+dx[k]<n and 0<=j+dy[k]<n:
                    if chess[i+dx[k]][j+dy[k]] == 0:
                        if check[index_2] == True:
                            continue
                        count_2[index_2]+=1
            index_2+=1


    max_1 = -1
    check_index=-1
    for i in range(n*n):
        if max_1<count[i]:
            check_index,max_1= i,count[i]
        elif max_1 == count[i]:
            if count_2[check_index]<count_2[i]:
                check_index,max_1 = i, count[i]


    check[check_index]=True
    chess[check_index//n][check_index%n]=lst[start][0]
    start+=1


print(chess)
'''



n=int(input())
chess=[[0]*n for _ in range(n)]
lst=[]

for _ in range(n*n):
    lst.append(list(map(int, input().split())))




dx = [-1,1,0,0]
dy = [0,0,-1,1]


check=[False]*(n*n)


#while문 돌게하려고
count_3=0
start=0

#while문 만들어야함.
while start<9:
    count = [0] * (n * n)
    count_2 = [0] * (n * n)

    #1번조건
    index=0
    #2번조건
    index_2=0

    #i:row / j:col
    for i in range(n):
        for j in range(n):
            #조건1번
            for k in range(4):
                if 0<=i+dx[k]<n and 0<=j+dy[k]<n:
                    for l in range(1,5):
                        if chess[i+dx[k]][j+dy[k]] == lst[start][l]:
                            if check[index] == True:
                                continue
                            count[index]+=1
            index+=1

            for k in range(4):
                if 0<=i+dx[k]<n and 0<=j+dy[k]<n:
                    if chess[i+dx[k]][j+dy[k]] == 0:
                        if check[index_2] == True:
                            continue
                        count_2[index_2]+=1
            index_2+=1


    max_1 = -1
    check_index=-1
    for i in range(n*n):
        if max_1<count[i]:
            check_index,max_1= i,count[i]
        elif max_1 == count[i]:
            if count_2[check_index]<count_2[i]:
                check_index,max_1 = i, count[i]


    check[check_index]=True
    chess[check_index//n][check_index%n]=lst[start][0]
    start+=1

dap=0
for i in range(n):
    for j in range(n):
        dap_help = 0
        for k in range(n*n):
            if chess[i][j] == lst[k][0]:
                for l in range(4):
                    if 0<=i+dx[l]<n and 0<=j+dy[l]<n:
                        for m in range(1,5):
                            if chess[i+dx[l]][j+dy[l]] == lst[k][m]:
                                dap_help+=1
        if dap_help == 1:
            dap+=1
        elif dap_help == 2:
            dap+=10
        elif dap_help == 3:
            dap+=100
        elif dap_help == 4:
            dap+=1000

print(dap)