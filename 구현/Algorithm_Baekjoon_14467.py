import sys
input = sys.stdin.readline

n = int(input())
lst = []
lst_2 = [False]*10
for _ in range(n):
    a,b = map(int,input().split())
    lst.append([a,b])

#print(lst)
num=0
for i in range(n):
    check_num = lst[i][1]
    for j in range(i+1,n):
        if (lst[i][0] == lst[j][0]) and (check_num != lst[j][1]) and (lst_2[lst[i][0]-1]) == False:
            num += 1
            check_num = lst[j][1]

    lst_2[lst[i][0]-1] = True

print(num)
