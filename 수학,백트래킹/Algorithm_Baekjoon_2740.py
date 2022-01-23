#2740번 행렬의 곱셈
mylist=[]
mylist2=[]
dap_list=[]
result=0
row1, col1 = map(int, input().split())
for row in range(row1):
    mylist.append(list(map(int, input().split())))

row2, col2 = map(int, input().split())
for row in range(row2):
    mylist2.append(list(map(int, input().split())))

if row1 == col2:
    if col1 == row2:
        for row in range(row1):
            for col in range(col2):
                result=0
                for i in range(col1):
                    result += (mylist[row][i]*mylist2[i][col])
                dap_list.append(result)
    else:
        print(-1)
else:
    print(-1)

check=0
for i in range(row1*col2):
    print(dap_list[i],end=" ")
    check+=1
    if check==row1:
        print()
        check = 0
