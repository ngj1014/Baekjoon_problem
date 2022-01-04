#둘다 양수이거나 둘다 음수일 때,힘들다.

n,m=map(int,input().split(' '))
array=list(map(int,input().split(' ')))
array.sort()
array_positive=[]
array_negetive=[]
for i in range(n):
    if array[i]<0:
        array_negetive.append(array[i])
    elif array[i]>0:
        array_positive.append(array[i])

array_positive.sort(reverse=True)
if array_positive==[]:
    maximum=-array_negetive[0]
elif array_negetive==[]:
    maximum=array_positive[0]
else:
    maximum=max(array_positive[0],-array_negetive[0])

sum=0
for i in range(0,len(array_negetive),m):
    sum-=array_negetive[i]

for i in range(0,len(array_positive),m):
    sum+=array_positive[i]

sum=2*sum-maximum
print(sum)