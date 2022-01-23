#전자레인지
#단위는 초 이다. 5분, 1분, 10초를 표시함
n = int(input())
mylist=[300,60,10]
countlist=[0,0,0]

for i in range(len(mylist)):
    countlist[i]  = (n//mylist[i])
    n%=mylist[i]

if n != 0:
        print(-1)
else:
    for i in range(3):
        print(countlist[i],end=" ")