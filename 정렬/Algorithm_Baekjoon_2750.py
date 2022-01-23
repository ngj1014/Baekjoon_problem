#정렬 2750번
n=int(input())
mylist=[]
for i in range(n):
    mylist.append(int(input()))
mylist.sort()
for i in range(n):
    print(mylist[i])
