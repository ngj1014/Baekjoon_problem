'''숫자 카드 게임'''
n, m = map(int, input().split())
mylist=[0 for _ in range(n)]
for i in range(n):
    mylist[i]= list(map(int, input().split()))
    #mylist.append(list(map(int, input().split())))도 가능하다.
for i in range(n):
    mylist[i].sort()

max=mylist[0][0]

for i in range(n):
    if max<mylist[i][0]:
        max=mylist[i][0]

print(max)

