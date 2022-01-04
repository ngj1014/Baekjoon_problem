m=int(input())
mylist=[]
count=0
for i in range(m):
    mylist.append(int(input()))

mylist.sort()
for i in range(m):
    count+=(abs(mylist[i]-(i+1)))

print(count)