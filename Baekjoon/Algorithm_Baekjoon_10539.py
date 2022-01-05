n=int(input())
lst=list(map(int,input().split()))

result=[]
count_2=1
count = 0
for i in range(n):
    result.append(lst[i]*count_2 - count)
    count+=int(result[i])
    count_2+=1
for i in range(n):
    print(result[i])