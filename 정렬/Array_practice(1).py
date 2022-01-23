#두 배열로부터 오름차순으로 배열
n,m=3,4
a=[1,3,5]
b=[2,4,6,8]
result=[0]*(n+m)
i=0
j=0
k=0

while i<n or j<m:
    if j>=m or (i<n and a[i]<b[j]):
        result[k]=a[i]
        i+=1
        k+=1
    else:
        result[k]=b[j]
        j+=1
        k+=1

for i in result:
    print(i)
