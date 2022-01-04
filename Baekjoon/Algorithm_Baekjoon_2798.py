#완전 탐색->100개의 카드가 있어도 최대 100만연산만하면되니 컴퓨터가 계산하기에 쉬움.. ->삼중 포무 이용하기.
n,m=map(int,input().split())
mylist = list(map(int, input().split()))
mylist.sort()
result=0
length=len(mylist)
for i in range(0,length):
    for j in range(i+1,length):
        for k in range(j+1,length):
            sum_value=mylist[i]+mylist[j]+mylist[k]
            if sum_value<=m:
                result=max(result,sum_value)

print(result)